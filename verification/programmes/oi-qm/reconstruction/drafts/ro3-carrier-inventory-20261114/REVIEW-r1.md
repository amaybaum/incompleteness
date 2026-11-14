ACCEPT WITH CHANGES — `RO3-INVENTORY-r1.md` at `0d6d8812a63cb90e5d41d14c2d5639a656096f38`

# Independent review of RO-3 inventory r1

## Standing of this review

- **Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro3-carrier-inventory-20261114/RO3-INVENTORY-r1.md`
  at `0d6d8812`. Its SHA-256, `7bb64895…f55f9`, matches the directory README. The commit's parent is
  `main` `dfeec843`, the stated base, and `origin/main` is still at that commit.
- **Mandate read.** #1055 comment 6881390849 (authorization and controls) and comment 6880024537
  (scope), both read through the public API. The supporting comments (#914 c.6875046763; #1169
  c.6876591512, c.6877981234) and the ledger r8 at `9ff3b8d9` were checked against the quotes in
  the inventory. Every quoted phrase is verbatim.
- **Method.** Paper-only. Every status cell in §1 was checked against `main` with `git show
  origin/main:<path>`: papers, Lean source text, the census JSON, the audit records and the SUBSTATE-1
  directory. Nothing was built or run. "Reviewer reading" marks an argument made in this review. None
  is verified, and none is offered as established.
- **Line numbers** below are lines of the inventory file.

## Summary

The comparison table is accurate in almost every cell. Citations resolve, Lean line numbers and
census family numbers (34, 40, 114, 120) are correct, and the three-carrier separation in §0 is
sound. I found no witness-to-theorem, finite-to-universal or conditional-to-unconditional upgrade in
a cell resting on `main`. All five binding controls hold in the inventory proper.

The findings are of four kinds:

- one cell whose status rests on the inventory's own reading, against its stated convention;
- two scope imprecisions;
- three omissions that change the first missing step for I-qloc and G-fam: an existing normalized
  state in the kernel, and on-`main` research instances of finite invariant stages and of factor maps;
- a recommendation that is well posed but discriminates less than §3 claims.

None requires restructuring. Each change is local.

## Findings

### Major

**M1. The recommendation (OBL-RO3-1) is close to definitional, and its positive branch does not meet
the target's reading of "one fixed model". Lines 346–387.**

- (a) at lines 358–360 follows almost immediately. `F` commutes with translations, so the
  configurations periodic under `L e_j` form a set that `F` and `F^{-1}` map into itself. Restricted
  to that set, `F` is the torus update by construction. The "if (a) fails" branch (line 367) is
  therefore close to vacuous, and the decision rule decides little.
- A periodic sector `P_L` is a global constraint: periodicity across the whole infinite lattice. It
  is not a subsystem. Gate A answer 3 requires one model to "support **subsystems** realizing every
  quantum carrier" (#1169 c.6876591512), and answer 4 requires closure under accessible
  preparations. A preparation confined to `P_L` fixes the state on infinitely many sites, so an
  embedded observer with finite access cannot perform it.
- Under sector confinement the prior's support is finite. The positive branch therefore restates
  total finiteness at the level of the state's support. It does not weaken A1. Lines 365–366 call
  confinement "an assumption the lemma does not justify", but they do not say that this assumption
  is a support-level finiteness posit of the same kind as A1. The finite-access control
  (#914 c.6875046763) needs that said.
- Line 384 says OBL-RO3-1 is "the missing embedding of G-fam (2.2)". That holds at the level of
  configuration sets. It does not hold at the level of one model with one prior. With any prior of
  full support on the infinite lattice the sectors have measure zero, as line 379 itself says.
- **A more discriminating candidate.** Reviewer reading, unverified; to be checked against Halmos and
  Rokhlin on automorphisms of compact abelian groups. Take the linear rule (posit (vii), Main:724) for
  prime `q = p` and `α ≢ 0`.
  - `F` is a continuous automorphism of the compact group `((Z/p)^2)^{Z^d}`, so it preserves Haar
    measure. Haar measure is the uniform product measure, which is the diagonal of the kernel's
    tracial reference state (M2).
  - On the dual module, `F` satisfies `t² − A t + 1 = 0` with `A` a nonconstant Laurent polynomial.
    So `det(F^n − I) = 2 − C_n(A) ≠ 0`, where `C_n` is the degree-`n` Chebyshev/Dickson polynomial.
    The dual action then has no nontrivial finite orbit, Haar measure is ergodic, and so it is mixing.
  - By the inventory's own note (lines 129–133), no finite cylinder partition with cells of measure
    in `(0, 1)` then has an exact common visible return at any positive time.
  - Consequence: under the interface's canonical uniform preparation, 1.2 is refuted on the
    completion, and the recurrence route to 1.3 is unavailable there.
  - This decides the G-nest versus completion question directly. The choice of prior is not made
    because it reproduces quantum predictions: it is the preparation the interface already assumes
    (`RegionTower.lean`, header item (3)).
  - Suggested change: §3 either adopts this as the obligation, or lists it beside OBL-RO3-1 and
    states OBL-RO3-1's limits as above.

**M2. I-qloc omits the normalized state already in the kernel. Lines 295–297, 304–308, 413–415.**

- `referenceState` (`QuasilocalAlgebra.lean:901`, with `referenceState_stage` at :904–905; audit
  `verification/audits/operational/quasilocal-completion-audit.md:212`) is a normalized tracial state
  on the completion, built from the consistent uniform family (`uniformFamily_isStateFamily`, :887).
- Main:588 says that no state is *selected* at the level of the laws. It does not say that none
  exists. So line 295 ("no rooted law is defined until a normalized invariant state … is supplied")
  and line 304 (first missing step: such a state) overstate the gap.
- The first missing step is invariance of `referenceState` under `heisQ`. A literature lead is not
  needed for that:
  - for the linear rule, Haar invariance under a continuous group automorphism is immediate;
  - in general, `τ ∘ heisQ` is again a tracial state.
- The Hedlund lead at lines 306–308 is unnecessary for the linear rule. Q6 (line 413) should name
  `referenceState` as the existing candidate, with its status: it exists in the kernel, and its
  invariance is not stated.

**M3. The negative searches of §5 miss on-`main` research instances, and the G-fam first missing
step omits factor maps. Lines 240–245, 264–266, 434–438.**

- `continuous-substates/README.md:105–107` states that `(Z/N)^{2L}` is a finite `F`-invariant
  subgroup of the torus `(R/Z)^{2L}`, and that its uniform measure is the finite substratum with
  alphabet `Z/N`. That is a nested family of finite invariant stages, of every alphabet size, inside
  one fixed model. It is an RR instance for G-nest, for the free 1-D map.
- `README.md:113–121` and :135–137 give the `p`-adic case. The finite models `(Z/p^k)^{2L}` are
  *factors* of one fixed model `(Z_p)^{2L}` under Haar, and the lowest-digit readout returns
  exactly.
- Line 241 requires "an injective map of stage `n` into stage `n+1`, or into one completion". A
  projective system of factor maps that intertwine the dynamics and push the prior forward also
  makes each member's rooted law a marginal of one fixed model. It avoids the measure-zero problem of
  line 379, and on `main` it has an RR instance. Add it to 2.2 and to §5, as RR context only
  (§A.46 item 7).
- Neither search phrase list at lines 434–436 covers "invariant subgroup". §5's bounded-phrase
  caveat at lines 440–441 is accurate, but the negative statement at line 266 should be narrowed to
  "for the `Z/q` lattice update", with these RR items listed.

### Medium

**m1. A cell's status rests on [IR], against the inventory's own rule. Line 126 against lines
56–57.** The 1.2 I-meas cell says "refuted within mixing systems [IR, see note]". Line 57 says that no
cell's status rests on an [IR] item, and line 48 requires a result on `main` for "refuted within".
The argument at lines 129–133 is correct as a reading. Move it to context and leave the cell at
"conditional[…]; open otherwise".

**m2. The scope of Main:155 is overstated. Lines 112 and 317–318.** Main:155 concerns
continuous-time Hamiltonian mixing flows. What it refutes is near-total *visible* common return at
every *sufficiently late* time. 1.1 is defined as microscopic `φ^L = id` (line 103). State the
source's scope exactly: continuous time, visible-cell return, sufficiently late times. Or give the
1.1 reading separately as [IR].

**m3. 1.4 G-nest rests on an unrecorded transfer. Line 162.** "Follows from F on the stage; not
stated separately" is the inventory's own reading, yet it is labelled conditional.

- The kernel theorem (`finiteRootedRealizable_iff_pper`, via `RootedRealization`) needs a product
  carrier `V × H` and one root-shared prior.
- A finite invariant stage need not be a product. GR:587's constraint surface correlates interior
  and exterior and uses fibre priors.

Mark the cell [IR], or add "the stage is a product `C_V × C_H'` with a root-shared prior (H-product
on the stage)" to its hypotheses.

**m4. A condition is missing from a conditional cell. Line 196.** Main:588 lists, besides the
state-mixing operation, the phases as "a stated intervention principle rather than a consequence of
its finite states and bijective dynamics". Every condition goes into the conclusion. Add the phase
intervention principle to the brackets. The statement concerns operational theories on finite
carriers (carrier 3), not the completion, so say so in that row. It is not a property of I-qloc.

**m5. A status is cited only to the off-`main` ledger. Line 197 against line 450.** The I-deep / I-meas
"open" cell in 1.7 cites only ledger items M5, J-3 and J-4, while §6 says that every status is traced
to a source on `main`. Add on-`main` sources: Main:556 (the all-horizons fixed-representation
question is open) and Main:588 (no characterization of infinite-dimensional instruments).

**m6. The #1055 controls are misidentified. Lines 204–205.** "These are the #1055 controls" refers to
1.1–1.6. The #1055 body also lists:

- the phase-locking lemma under (G1)–(G4);
- reverse finite realization;
- the observer-relative finiteness reading of #1053 and #1054.

None of these appears in 1.6. Either add them to 1.6 or drop the identification.

**m7. A resource statement omits an open condition. Lines 232–233.** With fixed-point registers, the
capacity bound's dependence on accuracy rests on the finite-`b` bound of clause (1), which is open
(Main:574, :596). The resources bullet should carry that condition.

### Minor

**n1. Kernel citations. Lines 107 and 121.**

- `rootedMap_periodic` (`RootedClassification.lean:135`) states that the rooted family is periodic,
  a visible statement. Its kernel content for `φ^L = id` is internal to the proof. The direct
  witness for 1.1 is `iterate_return_at_order` (`RootedRecurrenceBridge.lean:47`).
- Conversely, 1.2 F says "established (P)" when there is kernel support:
  `rootedMap_at_order` (`RootedRecurrenceBridge.lean:55`, census 114) and `rootedMap_periodic`.

**n2. Rooted conventions. Line 126.** `measuredGamma_eq_one_iff` uses the cell-conditioned ratio,
with an arbitrary measure and positive, finite cell masses. Its docstring says that invariance is not
used. The 1.2 header (line 115) says "under one root-shared normalized prior". Note the convention in
the cell. Lines 324–327 note it only later.

**n3. The `L ≥ 3` restriction. Lines 268–269 and 359–360.** Under SM:296's operator definition
`A = α Σ_j (T_j + T_j^{-1})`, the periodic sector equals the torus model for every `L ≥ 1`. The
restriction matters only for a simple-graph adjacency convention, as in SM:1602's circulant for
`L = 2`. Name the convention.

**n4. "Countable completion" is a misnomer. Lines 361 and 368–369.** `∪_L P_L` is a dense,
countable invariant *subset*, not a completion. It is directed by divisibility (`P_L ⊂ P_{kL}`),
not by `L → L+1`.

**n5. Readings that are cheap to decide.** These are reviewer readings, unverified. The labels are
correct as defined (line 50, relative to `main`).

- 1.1 I-qloc (line 111), for the linear rule at prime `q`: `det(F^n − I) ≠ 0` on the Laurent module,
  so no nonzero finitely supported configuration is periodic, and `φ^L ≠ id` for every `L`.
- 1.4 I-meas (line 163): the Bernoulli shift on `{0,1}^Z`, read at coordinate 0 with a root-shared
  product prior, realizes `Γ_0 = I`, `Γ_t = J` for `t ≥ 1`. That is a non-periodic realizable family.
  It is the elementary analogue of the RR XOR construction.

Both readings could go into §3's secondary candidates.

**n6. The update and its kernel object. Line 356.** `F(u,v) = (v, Av − u)` is the posited linear rule
(Main:724, item (vii)). Name the posit. The rounded bijection of SM:294 is outside OBL-RO3-1. The
kernel object for the infinite-lattice second-order rule is `ruleDynamics`
(`SecondOrderDrive.lean`, cited at Main:724).

**n7. Ledger standing. Lines 31–35.** The owner accepted r8 at `9ff3b8d9` (#914 c.6880700869, quoted
in the branch README at `4470bd02`). r9 is now on that branch. Citing the owner acceptance is more
exact than "the README lists it as reviewed".

## The controls in the authorization

| Control | Verdict | Where |
|---|---|---|
| Finite-carrier results preserved | holds, except that line 205 misnames the #1055 control set (m6) | §1.1–1.6, §2.1 |
| Finite access kept separate from total finiteness | holds in §0–§2. The positive branch of OBL-RO3-1 reintroduces support-level finiteness without saying so (M1) | lines 59–80, 186–188 |
| No infinite system assumed to inherit recurrence | holds. Every infinite-class cell is open, conditional or refuted, never inherited | 1.1–1.4 |
| A1 stays a posit | holds | lines 63–66 |
| No completion chosen for quantum reproduction | holds | Q1, Q6 |
| A family of finite models is not one model | holds | §2.2, lines 225–227 |

## First missing proof step, per class

- **F, I-deep, I-meas, I-nonorm:** correctly identified.
- **G-fam:** the step is correct, but stated too narrowly. Factor maps are an alternative to
  injective embeddings (M3).
- **G-nest:** correct for the `Z/q` lattice. The RR instance of a finite invariant subgroup should be
  listed (M3).
- **I-qloc:** misidentified. A normalized state exists in the kernel, and the missing step is its
  invariance under `heisQ` (M2).

## The recommendation

It is well posed and honestly labelled: "Recommendation, not a decision" (line 348), with [IR]
markers. It needs no new premise. But it discriminates less than lines 383–387 claim, for the reasons
in M1. Its positive branch is close to certain in advance, and it leaves the target's subsystem and
accessible-preparation requirements untouched. Revise §3 as M1 suggests.

## Owner questions

Q1–Q9 are the right questions. Add three:

- **Q10.** Does a sector, a restriction of the state's support that requires a preparation over
  infinitely many sites, count as a "subsystem" under Gate A answer 3, and as an accessible
  preparation under answer 4?
- **Q11.** Is the kernel's tracial reference state, the interface's own canonical preparation, to be
  examined as the completion's prior, without selecting it for quantum reproduction? This sharpens
  Q6.
- **Q12.** #1055 lists test case D2: can a fixed finite `S` accommodate a growing horizon? The
  inventory does not address it. Is it in RO-3's scope?

## Off-`main` references (§A.42 item 8)

The §6 trace is complete apart from m5. The ledger is used for row identifiers and one attributed
reading (§8.5). It also serves as the sole source of one status cell (line 197), which must get an
on-`main` source. The #1055, #1169 and #914 comments are governance references and support no
scientific claim.
