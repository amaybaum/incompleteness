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

The hypothesis is not a weakening of what was proved. Without it the direction fails within Lemma 3a's family for
d ≥ 2: CI at α = 1 has μ = 2(d − 1). At d = 3 that is K(0,1) = (B − 2)(B + 2), with {B + 2, ε} = 4ε ≠ 0 (row U1). The
family qualifier is load-bearing. For every (C, α), F = K T₀⁻¹ Π₋ + T₀ Π₊, with Π± = ½(1 ± ε), is local,
anticommutes with ε and squares to K (check G6, at d = 2 and 3). Chirality therefore constrains C only relative to
the isotropic staggered family with a scalar on-site mass. α = 1 is the unit coefficient of the
substratum-level rule (SM §4.2, "the two roles of the dynamics"), read here as a real lift. The descent of α = 1/d to the observer level is
the open bridge of SM §4.1.

## (2) The converse

**False as displayed.** The Remark's rule, C = 2(1 − d) at α = 1, has μ = 0. It factorizes through the massless
B, with {B, ε} = 0, while C = −4 ≠ 0 at d = 3 (row RM). The counterexample is valid against the display, whose
"lattice dynamics" fixes no α. At α = 1/2, d = 3, C = −1 is a second chiral, center-dependent rule (row H).

**True at fixed α = 1/d within Lemma 3a's family (SM Proposition 3b).** The hypotheses are λ ≠ 0, characteristic 0
and even extents ≥ 4. Suppose B′ + m or B′ + mε anticommutes with ε. The anticommutators are 2mε and 2m (the kernel
identity `Chiral.center_anticommutator`). Since ε is invertible, m = 0. Then λμ = 0, so μ = 0, and μ = C at α = 1/d. Row T2 is the countercheck: α = 1/d with C = 2(1 − d) is center-dependent and massive (μ = −4,
K = (B + 2ε)²).

**The structure.** Within the family, chirality is C + 2dα = 2. This is the constant-preserving normalization p₀ + 2dp = 1 of SM
Corollary 1b, with C = 2p₀ and α = 2p: in every row, chirality coincides exactly with K annihilating constants.
CI is C = 0. The two are independent conditions on (C, α) and meet only at Theorem 1's point (0, 1/d). This is the
POSITIVE gem-mode finding (§A.31): the display had merged two conditions, and Corollary 1b's two clauses are exactly
"massless" and "center-free".

## (3) Hypotheses that make the converse true

- **H1 (proved).** The hopping is fixed at α = 1/d, with the emergent fermion in Lemma 3a's family (isotropic
  staggered operator, scalar on-site mass), λ ≠ 0, over a field of characteristic zero, on even periodic extents of
  at least 4 for the coefficient identification. Under H1 chiral ⇒ CI holds: this is Proposition 3b. Its first step
  is the first-order on-site lemma, that {B′ + C_on, ε} = 2C_on ε vanishes only for C_on = 0. That lemma is
  derived independently on the owner's draft #965, which is credited here for priority.
- **H1′ (proved; it is Corollary 1b).** Constant preservation is imposed. Then the rule is chiral for every α, and CI
  holds exactly at α = 1/d. This is not a converse of Theorem 3: chirality is automatic there.
- **Open.** Two cases are not addressed: anisotropic or next-nearest-neighbour rules, and on-site masses that are
  operator-valued rather than scalar. Without some family restriction no converse holds (G6).

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
- **SM :296 ("the two roles of the dynamics").** It listed the Susskind factorization in the structural chain read
  by the exact unit-coefficient rule. The site now states α = 1/d for the massless factorization, and the mass
  m² = 2(d − 1) at the unit coefficient within Lemma 3a's family. No structural result of that paragraph uses
  chirality at α = 1.
- **Main, appendix-a, appendix-b, glossary, ch06, ch19, the companions.** No use of Theorem 3 or of CI ⟺ chiral.
- **Lean census.** Theorem 3 is not registered.

No physical claim loses support. The Higgs-necessity argument uses only the proved direction. It already
needed α = 1/d, and now says so.

| Site | Was | Anchor | Now |
|---|---|---|---|
| SM §4.3 Theorem 3 | "Center independence of the lattice dynamics is equivalent to exact chiral symmetry" | Its two proof lines (Theorem 2 on Theorem 1's branch); this record's G2, G4 T1 | One direction: at α = 1/d, C = 0 is the square of the massless staggered operator (chiral), and a mass m ≠ 0 gives C = ±m² with a₀ = 1. ID `SM:T-3` kept. |
| SM §4.3 (new) | none | Generator relations; G1–G3, G5 | Lemma 3a: K(C,α) = B² − μ, μ = C − 2(1 − dα), {B, ε} = 0, with coefficient identification at extents ≥ 4. New ID `SM:L-3a`. |
| SM §4.3 (new) | none | `Chiral.center_anticommutator`; #965's on-site lemma; G4 T1, T2 | Proposition 3b: at fixed α = 1/d, within Lemma 3a's family, with λ ≠ 0, characteristic 0 and even extents ≥ 4, chiral ⇒ C = 0. New ID `SM:P-3b`. |
| SM §4.2 :296, "the two roles of the dynamics" | The Susskind factorization (Theorem 2) is listed in the structural chain read by the exact unit-coefficient rule | Theorem 2 (Theorem 1's branch); Lemma 3a; G4 U1 | The factorization is massless at α = 1/d. At the substratum rule's unit coefficient, within Lemma 3a's family, it carries m² = 2(d − 1), nonzero for d ≥ 2. |
| SM §4.3 Remark | "C = 2(1−d) is not a mass term … the 4D staggered factorization has exact chiral symmetry" | Lemma 3a; G4 RM, U1 | Masslessness is C = 2(1 − dα), Corollary 1b's normalization. C = 2(1−d) at α = 1 is chiral and center-dependent, and C = 0 at α = 1 has, within Lemma 3a's family, m² = 2(d − 1), nonzero for d ≥ 2. The F construction shows the family hypothesis is load-bearing. The fixed α is load-bearing. "This lemma" is named: Lemma 3a or Theorem 3. H-link sentence kept. |
| SM §4.3 "Revised chain" | "Center independence implies the chiral statement of Theorem 3 on the staggered branch"; "Any claim that one algebraic CI condition simultaneously forces memory and chirality is therefore unavailable" | Theorem 3; Main's readback lemma and recurrence-cycle theorem | "Scope in the chain": "… on the normalized branch α = 1/d". "Revised" dropped (§A.33). The last sentence becomes a status statement: memory and chirality rest on separate results, and CI alone does not yield both. SC-17's ch05 :95 cites this content and still finds it. |
| `verification/lean/ROADMAP.md` §D | "center independence of the diagonal of D_st is equivalent to exact chirality" | `Chiral.center_anticommutator` is an identity | The identity is kernel-checked. The step to m = p₀ = 0 is not. Theorem 3 / Proposition 3b at α = 1/d, and the separation off it. |
| `OI_Structural_Core.lean` :413, docstring | "zero iff the center terms vanish" | The declaration is an identity | "an identity, not coefficient uniqueness" (#966's text). Comment only. |
| `structural_chain_probe.py` C3 docstring and print | "… iff exact chirality"; "center-free in D_st ⟺ exact chirality" | C3 checks identities in integer matrices | #966's text: "separate mass and scalar-offset anticommutator identities … not a universal converse". Documentation and print only. |
| `verification/coverage/LEDGER.json` | `SM:T-3` K2, fingerprint `487eed57…` | Census at this head | `SM:T-3` re-affirmed at `1f332468…`, graded K1: the α-weighted square is not in the kernel. `SM:L-3a` and `SM:P-3b` added, both K1. No ID retired. |

## Owner decisions (owner, 2026-10-27)

Quoted from the owner's message, relayed by the coordinator:

> "Use SC-32's theorem correction, not #966's proposed SM replacement … Preserve #965 as supporting mathematics,
> incorporate #966's two compatible docstring fixes, and retain all necessary qualifications"

> "Approve downgrading SM:T-3 from K2 to K1 … Record the precise proof coverage, retain existing valid
> certificates, and do not upgrade the result again without a corresponding machine-checked theorem."

**The route.**
- SC-32's text is the SM correction.
- #965's first-order on-site lemma is credited as the first step of Proposition 3b.
- #966's two docstring fixes are adopted, as described above.
- #966's SM replacement is not adopted.

**The downgrade.** `SM:T-3` goes from K2 to K1, keeping its ID. The existing Lean checks stay named in the ledger.

**What the Lean declarations prove:**
- **`Staggered.factorization`** (`OI_Staggered_Relations.lean`): (Σ_{i<n} A_i)² = Σ_{i<n} S_i², with S_i = t_i − s_i,
  for every n, with unit coefficients and abstract generators. There is no t·s = 1, so S_i² is not
  T² + T⁻² − 2, and there is no site parity ε. A_i² = S_i² is the separate theorem `A_sq`. The theorem does not cover
  the α-weighted square of Lemma 3a.
- **`Chiral.center_anticommutator`** (`OI_Structural_Core.lean`): the identity {D + m·ε + p₀, ε} = 2m + 2p₀·ε. It
  takes {D, ε} = 0, ε² = 1 and the commutation of m, p₀ with ε as hypotheses. It does not conclude m = p₀ = 0.
- **`Chiral.mass_square`**: (D + m·ε)² = D² + m·m. Its hypotheses are exactly ε² = 1, Dε = −εD, mε = εm and
  mD = Dm. It has no p.

**What each statement rests on:**
- **SM:T-3.** {B, ε} = 0 is not kernel-checked; only additivity is (`Chiral.anti_add`). The generator–parity
  anticommutation is exact finite algebra (G1). The (B + mε)² form of the mass clause is `mass_square` applied under
  that unchecked hypothesis. The α-weighted square and μ = C at α = 1/d are exact finite algebra only.
- **SM:L-3a.** No kernel witness of the statement. Its proof rests on the paper argument and on G1–G3 and G5 of this
  record.
- **SM:P-3b.** No kernel witness of the statement. Its proof rests on the paper argument and on G4 T1 and T2 of this
  record.

The ledger grades L-3a and P-3b K1 through the related identities named in their rows, which cover specialized
pieces and not the statements. Those rows are unchanged here.

No upgrade of these entries is made without a corresponding machine-checked theorem.

**Sites outside this unit.**

- **Explainer :826, ch05 :95 and its FULL mirror :1424.** These are SC-17's lines (#963). At its head `e316cf92` they
  carry the normalization α = 1/d. They are not edited here.
- **Two documentation fixes adopted from #966.** These are #966's replacement texts, credited to that draft and
  applied by hand. Its generator was not run. Both agree with Lemma 3a's family and Proposition 3b, and both are
  comment or print text only:
  - `verification/lean/OI_Structural_Core.lean` :413, the docstring of `center_anticommutator`. "zero iff the center
    terms vanish" becomes "an identity, not coefficient uniqueness". The iff fails for operator-valued m, p₀
    (m = I, p₀ = −ε). Stripped of comments and docstrings, the file is byte-identical, and it has 551 lines before
    and after.
  - `verification/lean/structural_chain_probe.py`, the C3 docstring (:14–15) and print (:136). "center
    independence of the diagonal of D_st iff exact chirality" and "center-free in D_st ⟺ exact chirality" become
    "separate mass and scalar-offset anticommutator identities … not a universal converse" and "… in the tested
    integer matrices". The AST is identical once the module docstring and print calls are excluded. Run under
    `python3 -I` from a copy, the output differs only in that print line.

The frozen round records `round-cc-1/2` `controls.py` (R10) are history and are not edited.

**Re-grep** over `papers/*.md`, `book/*.md`, `verification/lean/*`, `verification/coverage/LEDGER.json`:

- **"is equivalent to exact chiral symmetry".** 0 hits.
- **"equivalent to center independence".** Two surviving hits, ch05 :95 and FULL :1424. Both are SC-17's lines,
  already rewritten on #963.
- **"therefore unavailable" in SM §4.3.** 0 hits.
- **"Revised chain".** 0 hits.
- **"zero iff the center terms vanish" and "center-free in D_st ⟺".** 0 hits in `verification/lean/`.

**Check.** `python3 theorem3_exact.py > theorem3_exact.out` reproduces the committed output byte for byte, and so
does `-O`. Arithmetic is exact (Fraction). The countercontrols are an unstaggered η, an odd extent, and a d-blind mass
formula; each is rejected. G6 is the family countercontrol: the chiral F with F² = K exists for every (C, α). The verdict lines are generated from the measured rows.

Regenerated: SM (`.tex`, `.pdf`).
