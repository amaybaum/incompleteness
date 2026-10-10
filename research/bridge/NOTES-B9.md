# NOTES-B9 — the SPEC side of HO-5: what transferring the certified matrix-level spectator theorem would need

Node B9 of `research/bridge` (round 2). Base L = `9f9f8257`. Evidence:
- [X] `experiments/b9_spec.py`: 7/7 PASS, VERDICT B9-EXACT. Run 1 is final; one pre-run edit is logged in the
  header (the gate tables are parsed from `CompositeDimension.lean` at L); the replay is byte-identical.
- [K] at L: `substratumClass_contextStable` (StructuralClosure.lean:261); `IsMonomial` (SubstratumInterface.lean:75);
  `ContextStable` (ImplementationLocality.lean:359); `cnotFun`, `pc`, `pt`, `sgn` (CompositeDimension.lean:741–758).
- [A] HO-5 v1 items 1, 4, 5 and HO-6 v1, at their labels (`inbox/`); claim (D) (Z/RESULT.md); stage 4 (`{flow, J}`
  forces `Q3`); D5 §1.3(i) (monomial seed).

**Question (round-2 directive).** SPEC(φ) at the matrix level is the theorem `substratumClass_contextStable`.
- What would a transfer of the monomial class's context stability from the matrix carrier to `W 3` need (HO-6's
  two-token dictionary)?
- Would it reduce A_miss to SPEC_P(J) alone?

## 0. Answer

- **A transfer needs three things. Two are exact algebra, one is a premise:**
  - (D1) the dictionary `M : W 3 → Herm(ℂ²⊗ℂ²)`, with its product law [X Y1];
  - (D2) its intertwining of the monomial images and of the DIM-1 gate [X Y2, Y3; B8 X1];
  - (T) an M→P availability clause: the pulled-back idle extension of every admissible one-token implementation
    maps the *pair's* cone into itself.
- **Only (T) carries cone content, and (T) for the monomial class is SPEC_P(φ) ∧ SPEC_P(NOT).** That is (b) for
  `R_z(φ)`, all `φ`, and for `nflip`, on each token. **Disguise test: FAILS.** The certified theorem supplies none
  of (T): at the matrix carrier the state cone is PSD by construction and every unitary preserves it.
- **HO-6's formulation is vacuous.** "`ContextStable` carried to spectator stability of the image operations on the
  image cone": the image cone `M⁻¹(PSD)` is `Q3`, on which every unitary image acts, whatever the class. The
  non-vacuous form is (T) on the pair's own cone.
- **Reduction: yes, but only as a relocation.**
  - Granting (T) for the monomial class, A_miss ⟺ SPEC_P(J) exactly (HO-5 item 1, identities [X Y7]).
  - (T) is itself SPEC_P(φ), so A_miss ⟺ (T)_monomial ∧ SPEC_P(J). The content is unchanged.
- **Neither half is redundant, and neither alone forces `Q3`.**
  - The transferred monomial class with `cnot` (and the NOTs, SWAP) generates a compact group whose identity
    component is the diagonal 3-torus [X Y4]. It is abelian, so exotic cones survive (B7-2, CONDITIONAL on (D) [A]).
  - SPEC_P(J) with `cnot` generates the full two-qubit Clifford group modulo phases, order 11520 [X Y6]. It is
    finite, so exotic cones survive ((D), finite case [A]; C5 census `d_low = 5/256` [A]).
  - Together they are non-abelian: `V Z V*` is off-diagonal [X Y5]. That gives a local `su(2)`, and stage 4's
    `{flow, J}` forces `Q3` [A].
- **New exact fact (Y6 with B3 X2).** `⟨cnot, actC J, actT J⟩` equals `⟨cnot, local octahedral group⟩`. Both have
  order 11520 and the first is contained in the second. So, given H2, **SPEC_P(J) is equivalent to (b) for the whole
  native octahedral local family on both tokens.** The finite H-sourced operations of B3 (`S`, `cyc3`, …) are the
  discrete half of A_miss. The phase flow, which the certified matrix theorem covers at level M, is the continuous
  half.

## 1. What the certified theorem says

- **Statement.** `ContextStable substratumClass`: for every finite `R`, `S` and every monomial `K` at `S`,
  `tensorOf 1 K` is monomial at `R × S`. The spectator is adjoined on the left.
- **What it is.** A statement about an *implementation class*: which operators are admissible implementations on
  which carrier. It contains no cone.
- **What it does not give.** At the matrix carrier, the composite's state space is the Kronecker product with the
  PSD cone by construction (T6 D1 [A]). The theorem therefore says nothing about any cone `K ⊆ W 3` other than
  `M⁻¹(PSD) = Q3`.

## 2. The transfer, clause by clause

| clause | content | status | evidence |
|---|---|---|---|
| (D1) dictionary | `M(ω) = ¼ Σ ω_μν σ_μ⊗σ_ν`, a linear isomorphism `W 3 → Herm(ℂ²⊗ℂ²)`; `M(prodState x y) = ρ(x)⊗ρ(y)` | exact | [X Y1] for the product law, symbolic in `x`, `y`; the isomorphism is standard [W] (the 16 products `σ_μ⊗σ_ν` are an orthogonal basis of Herm(4)) |
| (D2) gate | `M(cnot ω) = CNOT·M(ω)·CNOT`, with `CNOT = |0⟩⟨0|⊗I + |1⟩⟨1|⊗X`; `nflip = B(X)` | exact | [X Y2]: the kernel's `pc`/`pt`/`sgn` parsed at L, all 16 basis tables |
| (D2) monomial images | `B(diag(1, c+is)) = R_z(c, s)`; `M ∘ actT R_z = Ad(1⊗U) ∘ M` and `M ∘ actC R_z = Ad(U⊗1) ∘ M` | exact | [X Y3], symbolic under `c² + s² = 1`; Cliffords and the drive step in B8 X1 |
| (T) M→P availability | for admissible `K` at a token, `M⁻¹ ∘ Ad(1⊗K) ∘ M` maps the pair cone into itself | **premise**: for the monomial class this is SPEC_P(φ) ∧ SPEC_P(NOT) | [W] from (D1), (D2) |

**Disguise test of (T): FAILS.**
- Restricted to the class, (T) is (b) for the class's Bloch images: I3.150–I3.153, I3.165's clause, OI⁺-1's
  spectator clause at P. Round-1 B2-4 found the same by analogy; (D1) and (D2) now make it exact.
- The alternative (T′) "the pair cone is `M⁻¹(PSD)`" makes the transfer trivial and is `K = Q3`, circular from the
  other side.
- Through B6 (Theorem B1.1, [D]: CI run 38092042844 green), (T) at level P follows from (A) at level H for each
  operation. So the hidden-level form of (T) is H-OI_g for the monomial images (B5). It is again the spectator clause.

## 3. The reduction and its non-redundancy

- **HO-5 item 1** (CONDITIONAL [W]). The identities `cyc3 R_z(t) cyc3⁻¹ = R_x(t)` and
  `cyc3 = R_z(π/2) R_x(π/2)` are re-checked exactly here [X Y7]. With them, A_miss ⟺ SPEC_P(φ) ∧ SPEC_P(J). Granting
  (T)_monomial, A_miss ⟺ SPEC_P(J).
- **(T)_monomial alone does not force `Q3`.**
  - The generators `Z⊗I`, `I⊗Z`, closed under conjugation by `CNOT`, `X⊗I`, `I⊗X` and SWAP, span exactly
    `{Z⊗I, I⊗Z, Z⊗Z}`. These are all diagonal and pairwise commuting [X Y4].
  - So the closed group generated by `cnot` and the transferred class has identity component the diagonal 3-torus,
    which is abelian.
  - B7-2 (CONDITIONAL on (D) [A]) gives an exotic invariant cone. This agrees with the monomial seed of D5 §1.3(i) [A].
- **SPEC_P(J) alone does not force `Q3`.** `⟨cnot, actC B(V), actT B(V)⟩` acts on `W 3` by signed permutations and
  is finite of order 11520 [X Y6]. Claim (D) covers finite groups [A].
- **Both together.** `V Z V* = X` [X Y5], so the identity component contains the two circles about `z` and `x` on one
  token, which generate a local `su(2)`. Stage 4 [A]: `{flow, J}` with `cnot` and H1–H3 forces `Q3`.
- **The discrete half equals the native family.**
  - `⟨cnot, actC J, actT J⟩ ⊆ ⟨cnot, local octahedral⟩`, since `J = cyc3` is octahedral.
  - Both have order 11520 (Y6; B3 X2), so they are equal.
  - Hence, given H2, SPEC_P(J) is equivalent to (b) for every octahedral rotation on each token. Those are the
    operations B1/B3 showed to be H-sourceable as readout-respecting hidden permutations, and B4 showed are not pair
    instruments of K(Z_F) when (A) fails.

## 4. A Lean statement of the dictionary

`research/bridge/lean/BridgeDictionary.lean` (verbatim on `dev-bridge/b11-lemma` @ bbbefb72, run 38093576860) states
the dictionary on the kernel's own tensor `tensorOf`, the operation `ContextStable` uses:
- `pauli`, `tokMat v = ½ Σ v_μ σ_μ`, `dict ω = ¼ Σ ω_μν tensorOf σ_μ σ_ν`;
- the product law `dict_tens`, `dict_prodState` (D1);
- `monomial_extension_admissible`, the certified `substratumClass_contextStable` restated at the pair carrier: the
  idle extension of a monomial one-token operator is admissible on `Fin 2 × Fin 2`;
- `TransferClause 𝓘 K`, the clause (T) as a definition (a premise of nothing).

The intertwining (D2) is not formalized; it needs entrywise Pauli identities. It is exact in b9 Y2–Y3.

CI: run 38093576860 **did not** build the module: Build failure (23:02:28–23:04:23Z, job 114334767486). In `dict_tens` the `simp only [… Finset.sum_mul, Finset.mul_sum]` step nested the right-hand double sum with the second factor's index outside, so the termwise `ring` faced `X μ·Y ν` against `X ν·Y μ` and failed. The `first` fallback was not tried, because the error inside `exact (… by ring)` was recovered during elaboration rather than thrown. `dict_tens` and `dict_prodState` therefore print `sorryAx`. `monomial_extension_admissible` built on [propext, Classical.choice, Quot.sound]; `TransferClause` elaborated. BridgeLemma rebuilt in the same run with all 14 axiom lines standard. Untested fix for a later round: replace the `first` block by `simp only [Fin.sum_univ_four]` followed by `ring` (no index matching), or rewrite with `Finset.sum_comm` before the termwise step. The dictionary stays a draft (not [D]); its
exact content rests on b9 Y1–Y3 [X]. No dispatch remains this round.

## 5. Verdict

- **The transfer's needs, stated exactly.** (D1) and (D2) are exact [X]. (T) is the only substantive clause, and for
  the monomial class it is SPEC_P(φ) ∧ SPEC_P(NOT). As a bridge it is **FAILED** (disguise test).
- **Reduction of A_miss to SPEC_P(J).** CONDITIONAL on (T), which is SPEC_P(φ). It is a relocation, not a discharge.
- **Non-redundancy.** Each half alone leaves exotic cones (CONDITIONAL on (D) [A]); together they force `Q3` [A].
- **Gem classification.**
  - **ELABORATING**: HO-6's interface question is answered. The only clause a transfer adds is (b) for the class
    images, and the "image cone" form is vacuous.
  - **NEW**: SPEC_P(J) with H2 is equivalent to (b) for the full native octahedral local family (Clifford group of
    order 11520). A_miss splits into a continuous abelian half (the phase flow, certified at M, needing (T) at P) and
    a finite half (the native Clifford family, H-sourceable, needing (A) at H). Each alone leaves exotic cones;
    together they force `Q3`.
