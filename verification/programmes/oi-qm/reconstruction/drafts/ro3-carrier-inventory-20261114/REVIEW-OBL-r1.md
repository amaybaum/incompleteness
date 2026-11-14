ACCEPT WITH CHANGES — `OBL-RO3-2-r1.md` and `RO3-INVENTORY-r3.md` at `76ca4c3dc121067efa51a565220edc4f2553077a` (PR #1303)

# Independent review of OBL-RO3-2 r1 and RO3-INVENTORY r3

- **Reviewer.** An independent reviewer, not the writer. The review was paper-only and read-only: no
  computation, no Lean build, no edits.
- **Mandate.** #914 comment 6883249235, item 6.
- **Sources read.**
  - Both files at the commit above. Their SHA-256 values match the README rows.
  - `papers/SM.md` lines 294 and 296, `papers/Main.md` lines 60, 121, 135–143, 155, 157 and 724,
    and `papers/GR.md` line 587, all at `origin/main` = `dfeec843`, the unit's stated base.
  - `QuasilocalAlgebra.lean` (lines 904, 966–1000 and 1264), `SecondOrderDrive.lean:339`,
    `SecondOrderCircuit.lean` (`leap`, `leapEquiv`), `SecondOrderLayer.lean` (`Rule`),
    `ObservableMeasureReturn.lean:83`, `RecurrenceHorizon.lean:119`,
    `ObservableFactorRecurrence.lean:68`, and the `RegionTower.lean` header.
  - `verification/programmes/substratum/continuous-substates/README.md` lines 85–140.
  - PR #1303 review 5906337933, which states nits N1–N3.

## Overall

The central theorem is correct. On `X = ((F_p)^2)^{Z^d}`, with `p` prime, `α ≠ 0` and `d ≥ 1`, the
update `F(u, v) = (v, Av − u)` is mixing for the uniform product (Haar) measure. Steps 1–8 form a
complete paper proof from S1–S3. It needs no external theorem, so the unreached Halmos and Rokhlin
texts carry no weight. I found no gap at `p = 2`, at the boundary (there is none on `Z^d`) or in the
orientation.

One consequence is overstated and must be narrowed before acceptance: the heading of §3.2. Its
surrounding text also implies a false picture of the periodic points. The remaining findings are
minor.

## Findings by severity

### Required change

**R1. §3.2 (lines 203–210, summary row line 314): "Microscopic recurrence. Refuted on `X`" is
stronger than what is proved, and the text implies that only spatially periodic configurations
recur.**

- **What is proved.** `F^n ≠ id` for every `n ≥ 1`, and no nonzero finitely supported configuration
  is periodic. Both are correct.
- **Why the heading is too strong.**
  - Poincaré recurrence holds. `F` preserves a probability measure on a compact metric space, so
    `μ`-almost every point returns arbitrarily close to itself in the product topology.
  - For `d ≥ 2` the exactly periodic points are uncountable, and most of them are not spatially
    periodic.
- **Counterexample.** Take `d = 2`, any prime `p` and any `α ≠ 0`.
  - `F` fixes `(u, u)` exactly when `Au = 2u`.
  - Write this as `u(n_1 + 1, n_2) = 2α^{-1} u(n) − u(n_1 − 1, n_2) − u(n_1, n_2 + 1) − u(n_1, n_2 − 1)`.
    The recursion runs uniquely in both directions from any choice of the two columns `n_1 = 0, 1`.
  - So `Fix(F) ≅ (F_p^Z)^2`, which is uncountable.
  - Choose column `0` aperiodic in `n_2`. The resulting configuration is not invariant under any
    finite-index sublattice, so it is not spatially periodic.
- **Why the general case behaves the same way.** For every `n`, `Fix(F^n)` is dual to
  `R^2/(B^n − I)R^2`, read with the transpose convention.
  - The zeroth Fitting ideal of that module is `(δ)`, with `δ = det(B^n − I)`.
  - If the module were finite, `R/δ` would be finite. That fails for `d ≥ 2`.
  - The dual of an infinite countable discrete group is an infinite compact group, which is
    uncountable.
  - For `d = 1`, `Fix(F^n)` is finite and invariant under the shift, so there every periodic point is
    spatially periodic.
- **What remains true.** The set of periodic points is `μ`-null. Line 210 ("They form a countable
  set") does not establish this; it covers only the spatially periodic points. A one-line proof:
  - `Fix(F^n)` is closed and `F`-invariant;
  - by ergodicity its measure is 0 or 1;
  - measure 1 would make it all of `X`, because `μ` has full support and the set is closed, which
    contradicts `F^n ≠ id`.
- **Safe path.**
  - Retitle the subsection: "`F` has infinite order; periodic points are `μ`-null".
  - State that Poincaré recurrence holds `μ`-almost everywhere.
  - State that periodic points exist, uncountably many for `d ≥ 2`, and form a `μ`-null set, with
    the proof above.
  - In line 210, replace the countability sentence with that statement.
  - Apply the same change to the summary row (line 314) and to the cross-reference in §4.1
    (line 261, "(3.2)"), which stays correct once 3.2 carries the null-set proof.

### Minor

**m1. Line 281, the countercontrol with constant `a` (`α = 0`).** The map `(u, v) ↦ (v, −u)` has
order 4 only for odd `p`. For `p = 2` it is the swap and has order 2. The conclusion, periodic and
not ergodic, is unaffected.

**m2. Lines 256–257, §4.1.** SM:296's order theorem `F^{p(p^{2m}−1)} = I` is stated for `p ∤ L`
(and `L ≥ 2`); line 256 omits the hypothesis. For `p | L` the conclusion needed still holds trivially:
`F` is an automorphism of a finite group, so it has finite order and every dual orbit is finite.
State both cases.

**m3. Line 138 against lines 278–279.** Step 4(b) is declared "proved here for `X` only", but the
`p`-adic and real-torus countercontrols apply it to `(Z_p)^{2L}` and `(R/Z)^{2L}`. The proof uses only
the orthonormality of characters under Haar measure, so it carries over verbatim. Say so at line 138
or at the table.

**m4. Lines 196–198, §3.1.** The claim that Main's rooted maps coincide with the cell-conditioned
ones holds when the readout is the restriction `x ↦ x|_Λ` to a finite set of sites `Λ`. For a
coarse-grained readout `g(x|_Λ)` whose cells have unequal fibres in `Conf Λ`, there is no hidden prior
shared by every root in Main's product form. Restrict the sentence to `π = res_Λ`, or say that the
cell-conditioned convention is the one used.

**m5. Line 213, §3.3.** "Refuted" describes a route whose hypothesis fails here; "unavailable"
(line 315, §7) is the accurate word. The list also omits the near-return variant (the
continuous-time common near-total return of `papers/Main.md:155`). Mixing excludes near-total return
only at sufficiently late times, not at a bounded time. One sentence stating that scope would close
the item. The open status of P-indivisibility itself (lines 219–221) is correct.

**m6. Line 291, §5 (ii-b).** The stated condition can be checked directly from the definitions on
`main`.
- `heis Φ T = permOpInv Φ * T * permOp Φ` (`QuasilocalAlgebra.lean:999`).
- `permOp` is `mapDomain` along `φ`.
- `permOpInv_apply` gives `(permOpInv f)(t) = f(φ t)`.
- Hence `heis Φ D_f = D_{f ∘ φ}`.

Combined with `heisQ_stage` and (ii-a), this would reduce (ii-b) to Step 2. Leaving it conditional is
acceptable but conservative.

**m7. Lines 60–84, §1.** The mandate's first requirement, verifying Halmos and Rokhlin from primary
sources before applying them, is unmet. The unit handles this correctly: it does not apply them and
proves what it needs. The owner should still be told plainly that this mandate item is unmet,
together with the reason it does not affect the result. Standard textbook treatments of automorphisms
of compact abelian groups, such as Walters' introduction to ergodic theory and Schmidt's *Dynamical
Systems of Algebraic Origin*, state both criteria. This reviewer did not consult them either.

**m8. `RO3-INVENTORY-r3.md` line 401.** The sentence "Neither route is checked here" follows a
paragraph that now names only one route; the second route was folded into (i). Change "Neither route
is" to "This route is not".

## Step-by-step verdicts

### 1. The mixing criteria (Step 4, lines 125–138)

- **4(a): no periodic dual vector ⟹ mixing. Correct and complete.**
  - `B` is invertible (`det B = 1`), so the orbit of any `ξ ≠ 0` has no repeats.
  - `⟨U^n χ_ξ, χ_η⟩ = [B^n ξ = η]` is therefore eventually zero.
  - The extension to `L^2` uses unitarity of `U`, which needs `F` to be invertible and to preserve
    `μ` (Step 2), and density (S3).
  - Indicators then give `μ(E ∩ F^{-n} E') → μ(E) μ(E')`.

  This is the standard proof of "ergodic ⟹ mixing" for automorphisms of compact abelian groups,
  specialised to this `X`. Because it goes straight from the absence of periodic characters to
  mixing, (R) is not needed. That is correctly noted at line 180.
- **4(b): periodic dual vector ⟹ not ergodic. Correct.** The orbit sum is invariant, has mean zero
  and has norm squared equal to the orbit length.
- **Together.** (a) and (b) give the equivalence "ergodic ⟺ no nonzero periodic character ⟺ mixing"
  for this `X`. This is what (H) and (R) assert for general compact abelian groups. The identification
  of all of `X`'s dual with the finitely supported `ξ` is standard and not needed for either
  implication.
- **Group, map and continuity.** `X` is a compact metrizable abelian group. `F` is additive.
  Continuity is correctly argued from finite dependence. `F^{-1}(u', v') = (Au' − v', u')` is correct
  and also of finite range.
- **Step 2's appeal to Steps 3 and 5.** The forward reference is not circular: Steps 3 and 5 do not
  use Step 2.

### 2. The dual action and the determinant (Steps 3 and 5–7)

- **Step 3.** `⟨ξ, F x⟩ = Σ (−ξ_2) u + (ξ_1 + Aξ_2) v`. Moving `A` across the pairing uses symmetry
  of the kernel. Since `A` is symmetric here, orientation cannot matter. The column matrix
  `[[0, −1], [1, a]]` matches `B(ξ_1, ξ_2) = (−ξ_2, ξ_1 + aξ_2)`, with `tr B = a` and `det B = 1`.
  Correct.
- **Step 5.** Translation by `±e_j` becomes multiplication by `x_j^{±1}`; the sign convention is
  irrelevant because `A` is symmetric. `D_{n+1} = a D_n − D_{n−1}` follows from Cayley–Hamilton, and
  `det(M − I) = det M − tr M + 1` holds for 2 × 2 matrices. `P_n` is monic of degree `n` for `n ≥ 1`,
  including `p = 2`, where `P_0 = 0`. Correct.
- **Step 6.** The `x_1`-top coefficient of `2 − P_n(a)` is `−α^n ≠ 0`, because `α` is a unit of
  `F_p`; this does not even need `S` to be a domain. Correct for every `d ≥ 1` and every prime `p`.
  - The remark that every nonconstant Laurent polynomial is transcendental over `F_p` is also
    correct: an algebraic `a` lies in a finite field `F_p[a]`, so it is `0` or a unit of finite order;
    the units of `R` are the monomials `c x^m`; finite order forces `m = 0`.
- **Step 7.** The adjugate identity `adj(N) N = det(N) I` over the domain `R` gives `ξ = 0`. Correct.
- **Conclusion.** No gap at `p`, at the boundary (none on `Z^d`) or in the orientation.

### 3. Reconciliation with SM:294 (§4.1, lines 247–270)

Consistent. SM:294 asserts non-ergodicity of the exact linear rule on finite-torus energy shells. Its
grounds are further quadratic invariants and the order bound of the remark at SM:296.

- **The map.** SM writes the same map, `F(u, v) = (v, Av − u)` with `A = α Σ_j (T_j + T_j^{-1})`, on
  the torus `(Z/L)^d` instead of `Z^d`. The kernel's `leap` (`SecondOrderCircuit.lean`) is the same
  per-site form `(p, c) ↦ (c, F c − p)`.
- **The measure.** SM's measure is the uniform law on a finite shell. Here it is Haar measure on the
  infinite product.
- **Both carrier and measure differ.** The writer correctly says so:
  - the tori are `μ`-null invariant subsets carrying their own invariant measures;
  - energy sums on `Z^d` are not functions on `X`;
  - the real-lift integrability remark at SM:294 concerns a third carrier.
- **No contradiction remains.** Apart from m2, the account is accurate.

### 4. Countercontrols (§4.2, lines 272–283)

Each one fails where it should.

- **`p`-adic `(Z_p)^{2L}`.** Every element of the dual `(Q_p/Z_p)^{2L}` lies in the finite
  `B`-invariant subgroup `(p^{-k}Z_p/Z_p)^{2L}` for some `k`, so its orbit is finite. 4(b), as
  transferred (m3), gives non-ergodicity. This is consistent with lowest-digit exact return at the
  source.
- **Real torus `(R/Z)^{2L}`.** `M = F^L − I` is nilpotent, so `det M = 0`. The integer row vectors
  `v` with `vM = 0` are nonzero characters fixed by the dual of `F^L`. This is consistent with the
  exact return of the difference readouts at the source.
- **Finite `F_p` torus.** `a` is algebraic in `R_L`, so Step 6 fails. Correct, with m2.
- **`α = 0`.** Periodic, with m1.
- **Sources unchanged.** No countercontrol is altered at its source.

### 5. Consequences (§3 and §5)

- **§3.1, exact visible return. Correct.**
  - `measuredGamma_eq_one_iff` (`ObservableMeasureReturn.lean:83`) states exactly
    `Γ = 1 ⟺ μ(change event) = 0`, with positive and finite cell masses.
  - Iterating that equality relies on measure preservation.
  - Along `kn`, mixing forces `μ(C_a) ∈ {0, 1}`.
  - The limit `Γ_t(a, ·) → μ(C_·)` is also correct.
  - See m4.
- **§3.3, the recurrence route. Correct in substance.**
  - Every cited theorem (Main:121, 135, 141; GR:587; `RecurrenceHorizon.lean:119`;
    `ObservableFactorRecurrence.lean:68`) consumes an exact identity return.
  - P-indivisibility itself is correctly left open, and the readback lemma is correctly left
    untouched.
  - See m5.
- **§3.4, finite factors. Correct.**
  - The value `ν({y} ∩ S^{-n}{y}) ∈ {0, ν(y)}` cannot converge to `ν(y)^2`.
  - A continuous finite factor is covered as well: its fibres are nonempty clopen sets, which have
    positive measure because `μ` has full support.
- **§3.2.** See R1.
- **§5, the separation of statements.**
  - **(i), Haar invariance.** Kept separate.
  - **(ii-a), the bridge.** `referenceState_stage` (`QuasilocalAlgebra.lean:904`) gives
    `|Conf Λ|^{-1} tr X`, so on `diag(f)` it is the cylinder average. Correct.
  - **(ii-b).** Conditional; see m6.
  - **(ii-c), off-diagonal invariance.** Correctly open. The unique-trace route is plausible because
    `heisQ` is multiplicative and isometric (from line 1264 on), but it is not stated on `main`.
  - **(iii), physical realization.** Correctly open. The `RegionTower.lean` header item (3) names the
    uniform family as the interface's assumed preparation only.
  - **Owner's Q11.** Honored at line 242.
  - **No quantum or EXACT claim.** The unit claims no quantum realization and does not discharge
    EXACT (lines 240–241 and 331).

### 6. The r3 diff

`diff RO3-INVENTORY-r2.md RO3-INVENTORY-r3.md` at the commit contains:
- the title;
- the header;
- N2, at r3 lines 326–328;
- N3, at lines 381–382, 392–401, 452, 468–471 and 520;
- N1, at lines 483–486;
- Q10–Q12 with the adopted text, at lines 576–598;
- one §6 row, at line 640.

All of these are the three wording fixes, the Q10–Q12 record, or the header and §6 row that the
header itself discloses.

Two deletions inside Q10–Q12 go with recording the decisions:
- Q11's "OBL-RO3-2 assumes a yes for its own scope", now moot under the adopted decision;
- Q12's question "Is D2 in RO-3's scope beyond these citations?", now answered.

There is no other substantive change. See m8 for the one wording defect the edit introduced.

## Summary

The mixing theorem stands as proved on paper for prime `p`, `α ≠ 0`, `d ≥ 1` and Haar measure. Apply
R1. The minor items m1–m8 can land in the same revision.
