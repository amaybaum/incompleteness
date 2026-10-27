# SC-32: SM Theorem 3, displayed as an equivalence (#942 / #946)

Base: `main` at `0d917665`. Source: SC-17's two independent reviews. SM §4.3 Theorem 3 displayed "center
independence of the lattice dynamics is equivalent to exact chiral symmetry of the emergent staggered fermions".
Both lines of its proof show one direction, and its own Remark exhibits a center coupling, C = 2(1−d), with
exact chiral symmetry. The objects below are SM's own. The rule is φ(n,t+1) = Cφ(n,t) + α Σ_j[φ(n+ê_j,t) +
φ(n−ê_j,t)] − φ(n,t−1), and CI is C = 0 (§4.4). The staggered generators are A_μ = η_μ(T_μ − T_μ⁻¹), with
D_st = ½ Σ A_μ (Theorem 2). The site parity is ε = (−1)^{Σx}. Chirality is SM's criterion χ → εχ, that is {D, ε} = 0.
The staggered square produces two-step shifts, so the rule is read as K(C,α) = T₀² + T₀⁻² − α Σ_j(T_j² + T_j⁻²) − C.
Each coset of (2ℤ)^{d+1} carries the rule itself (check G3).

## (1) The direction proved

The mass identity (SM Lemma 3a) holds on even periodic extents. Take B = A₀ + b Σ_j A_j with b² = −α. Then
K(C,α) = B² − μ with μ = C − 2(1 − dα), and {B, ε} = 0. Within the isotropic staggered family with a scalar on-site
mass m, entering as (B′ − m)(B′ + m) or (B′ + mε)², the coefficients are fixed: m² = ±λμ. The proof uses only the
generator relations, the vanishing cross terms and the disjoint supports of I, T₀^{±2} and T_j^{±2}.

The original proof's two lines both use Theorem 2's factorization on Theorem 1's branch, so the direction they
prove carries the hypothesis α = 1/d. There μ = C. So C = 0 gives K = B², a massless operator that anticommutes
with ε, and a mass m ≠ 0 gives C = ±m² ≠ 0. This is SM Theorem 3, stated at that scope.

The hypothesis is not a weakening of what was proved. Without it the direction fails: CI at α = 1 has μ = 2(d − 1).
At d = 3 that is K(0,1) = (B − 2)(B + 2), with {B + 2, ε} = 4ε ≠ 0 (row U1). α = 1 is the unit coefficient of the
substratum-level rule (SM §4.2, "the two roles of the dynamics"), read here as a real lift. The descent of α = 1/d to the observer level is
the open bridge of SM §4.1.

## (2) The converse

**False as displayed.** The Remark's rule, C = 2(1 − d) at α = 1, has μ = 0. It factorizes through the massless
B, with {B, ε} = 0, while C = −4 ≠ 0 at d = 3 (row RM). The counterexample is valid against the display, whose
"lattice dynamics" fixes no α. At α = 1/2, d = 3, C = −1 is a second chiral, center-dependent rule (row H).

**True at fixed α = 1/d (SM Proposition 3b).** Suppose B′ + m or B′ + mε anticommutes with ε. The anticommutators are
2mε and 2m (the kernel identity `Chiral.center_anticommutator`). Since ε is invertible, m = 0. Then μ = 0, and μ = C
at α = 1/d. Row T2 is the countercheck: α = 1/d with C = 2(1 − d) is center-dependent and massive (μ = −4,
K = (B + 2ε)²).

**The structure.** Chirality is C + 2dα = 2. This is the constant-preserving normalization p₀ + 2dp = 1 of SM
Corollary 1b, with C = 2p₀ and α = 2p: in every row, chirality coincides exactly with K annihilating constants.
CI is C = 0. The two are independent conditions on (C, α) and meet only at Theorem 1's point (0, 1/d). This is the
POSITIVE gem-mode finding (§A.31): the display had merged two conditions, and Corollary 1b's two clauses are exactly
"massless" and "center-free".

## (3) Hypotheses that make the converse true

- **H1 (proved).** The hopping is fixed at α = 1/d, with the emergent fermion in Lemma 3a's family (isotropic
  staggered operator, scalar on-site mass) on even periodic extents over a field of characteristic zero. Under H1
  chiral ⇒ CI holds: this is Proposition 3b.
- **H1′ (proved; it is Corollary 1b).** Constant preservation is imposed. Then the rule is chiral for every α, and CI
  holds exactly at α = 1/d. This is not a converse of Theorem 3: chirality is automatic there.
- **Open.** Two cases are not addressed: anisotropic or next-nearest-neighbour rules, and on-site masses that are
  operator-valued rather than scalar. For the first-order operator alone, an on-site term C_on commuting with ε
  preserves {D, ε} = 0 only for C_on = 0. That independent derivation is the owner's draft #965, credited for
  priority and not adopted here. It concerns a different object from the second-order C.

None of these converses is kernel-certified. §A.34 asks for kernel witnesses per direction for a displayed
equivalence, so SM displays the two directions as separate statements, each with its own witness and scope.
SM's display therefore carries no "iff".

## (4) Downstream dependents

Every use found relies on the proved direction, on Theorem 1's branch, which is the branch all of §4 rides. None
uses chiral ⇒ CI.

- **SM :306 at the base, :316 here (now "Scope in the chain").** Uses CI ⇒ chiral. The scope α = 1/d is now stated.
- **SM :595 at the base, :605 here (§4.11, Higgs).** "Chiral symmetry (Theorem 3) combined with the center-independent gauge sector
  forbids explicit masses". This is CI ⇒ chiral on the normalized branch. Unchanged.
- **SM :543 at the base, :553 here (Theorem 13 proof).** Cites Theorem 3 for {D_st, ε} = 0, the massless operator. Unchanged.
- **SM :563 at the base, :573 here (Nielsen–Ninomiya).** "the exact chiral symmetry of Theorem 3, χ → εχ". Unchanged.
- **SM :236.** "center-free/chiral branch (§4.3)". Unchanged.
- **Main, appendix-a, appendix-b, glossary, ch06, ch19, the companions.** No use of Theorem 3 or of CI ⟺ chiral.
- **Lean census.** Theorem 3 is not registered.

No physical claim loses support. The Higgs-necessity argument uses only the proved direction. It already
needed α = 1/d, and now says so.

| Site | Was | Anchor | Now |
|---|---|---|---|
| SM §4.3 Theorem 3 | "Center independence of the lattice dynamics is equivalent to exact chiral symmetry" | Its two proof lines (Theorem 2 on Theorem 1's branch); this record's G2, G4 T1 | One direction: at α = 1/d, C = 0 is the square of the massless staggered operator (chiral), and a mass m ≠ 0 gives C = ±m². ID `SM:T-3` kept. |
| SM §4.3 (new) | none | Generator relations; G1–G3, G5 | Lemma 3a: K(C,α) = B² − μ, μ = C − 2(1 − dα), {B, ε} = 0, with coefficient identification. New ID `SM:L-3a`. |
| SM §4.3 (new) | none | `Chiral.center_anticommutator`; G4 T1, T2 | Proposition 3b: at fixed α = 1/d, chiral ⇒ C = 0. New ID `SM:P-3b`. |
| SM §4.3 Remark | "C = 2(1−d) is not a mass term … the 4D staggered factorization has exact chiral symmetry" | Lemma 3a; G4 RM, U1 | Masslessness is C = 2(1 − dα), Corollary 1b's normalization. C = 2(1−d) at α = 1 is chiral and center-dependent, and C = 0 at α = 1 has m² = 2(d − 1). The fixed α is load-bearing. H-link sentence kept. |
| SM §4.3 "Revised chain" | "Center independence implies the chiral statement of Theorem 3 on the staggered branch" | Theorem 3 | "Scope in the chain": "… on the normalized branch α = 1/d". "Revised" dropped (§A.33). |
| `verification/lean/ROADMAP.md` §D | "center independence of the diagonal of D_st is equivalent to exact chirality" | `Chiral.center_anticommutator` is an identity | The identity is kernel-checked. The step to m = p₀ = 0 is not. Theorem 3 / Proposition 3b at α = 1/d, and the separation off it. |
| `verification/coverage/LEDGER.json` | `SM:T-3` K2, fingerprint `487eed57…` | Census at this head | `SM:T-3` re-affirmed at `3a614162…`, graded K1: the α-weighted square is not in the kernel. `SM:L-3a` and `SM:P-3b` added, both K1. No ID retired. |

**Sites outside this unit.** Three overlap with open units and are left to them:

- **Explainer :826.** SC-17, #963.
- **ch05 :95 and its FULL mirror :1424.** SC-17, #963. SC-17's new wording, "On the staggered branch it gives exact
  chiral symmetry … a center-free rule carries none", is true only on the normalized branch. A follow-up there should
  name α = 1/d.
- **`OI_Structural_Core.lean`, docstring of `center_anticommutator`.** It reads "zero iff the center terms vanish".
  The Lean statement is an identity, and the iff fails for operator-valued m, p₀ (m = I, p₀ = −ε).

The owner's draft #966 covers two more, which are left unedited here:

- **`structural_chain_probe.py`, C3 docstring and print.** They read "center-free in D_st ⟺ exact chirality", which is
  the first-order statement, checked only as an identity.
- **The Lean docstring above.**

The frozen round records `round-cc-1/2` `controls.py` (R10) are history and are not edited.

**Re-grep** over `papers/*.md`, `book/*.md`, `verification/lean/*`, `verification/coverage/LEDGER.json`:

- **"is equivalent to exact chiral symmetry".** 0 hits.
- **"equivalent to center independence".** Two surviving hits, ch05 :95 and FULL :1424. Both are SC-17's lines,
  already rewritten on #963.
- **"Revised chain".** 0 hits.

**Check.** `python3 theorem3_exact.py > theorem3_exact.out` reproduces the committed output byte for byte, and so
does `-O`. Arithmetic is exact (Fraction). The countercontrols are an unstaggered η, an odd extent, and a d-blind mass
formula; each is rejected. The verdict lines are generated from the measured rows.

Regenerated: SM (`.tex`, `.pdf`).
