# EQ4 — the three-copy obstruction (EQ4-P) and the four-copy formalization package (EQ4-F): design-only protocol

**Status.** Research and design only. Nothing produced here is adopted, frozen or governed. Governance stays frozen:
- no F designation, round, branch, push, PR or CI dispatch;
- no ROADMAP or manuscript edit;
- no premise adoption.

The owner requested these threads after the EQ3 audit (`scratchpad/eqreview/EQ3-AUDIT.md`). Their order of priority:
1. resolve the mixed configuration;
2. investigate the CNOT Choi effect;
3. formalize the four-copy result;
4. preserve the governance boundary.

## The owner's decisive question

> Can consistency across larger composite systems force the required extension of operations without assuming uniform
> composition or introducing the extension principle in disguise?

A positive result makes the reconstruction stronger. A rigorous counterexample says exactly which further physical
principle is missing.

## Vocabulary (as in EQ3)

- **KT∞, composition coherence; state-level only.** For every finite family of tokens and every bipartition of it into
  two groups, the family's body is a COMP-1 composite of the two group bodies. Each group's body is the body of the
  composite of its members, and it carries all of its `IsEffectOn` effects [K KF:116, CI:227].
- **Instances** are named by token sets and groupings, e.g. KT(6; 012|345, 03|1425, 14|25).
- **Crossing constraint.** Let a family `S = A ⊔ B = C ⊔ D` have all four intersections nonempty. Then
  `⟨K_A* ⊗ K_B*, K_C ⊗ K_D⟩ ≥ 0`, and symmetrically. If one intersection is empty, the constraint follows from the
  subfamilies' coherence (coordinator's remark, written; check it).
- **Tags, as in EQ3 Amendment 1.**
  - (s) a state-level fact;
  - (2) an operation on a standalone two-token composite: the native gate, or its inverse;
  - (o) an operation on part of a larger composite. This is idle extension, and it is forbidden as a premise.
- **The owner's P/A/C rule.**
  - `P ∧ A ⇒ C` is sufficiency.
  - An exact model of `P ∧ ¬C` shows only that P alone does not give C.
  - Necessity of A relative to P needs a proof of `P ∧ C ⇒ A`.
  - Never write "required" or "necessary" without that proof.

## What is settled (do not redo; re-verify only what you rely on)

**Inputs:**
- `scratchpad/eq3/P/RESULT.md`, with its NOTES and scripts;
- `scratchpad/eqreview/EQ3-AUDIT.md` and the scripts `audit_eq3_n1.py` and `audit_eq3_n2.py`;
- `scratchpad/eqreview/EQ2-SYNTHESIS.md`;
- `scratchpad/eqreview/eq4_precheck.py` and its `.out`. These are coordinator pre-checks, not evidence for this thread.

**Settled facts:**
- **Two copies.** KT(4; 01|23, 02|13) gives three things, each pair cone in its token charts:
  - every pair cone is Q3 or the twin;
  - IE₁;
  - even 4-cycles.

  The premises: the transported two-copy premises on every pair, closedness and COMP-1 full effects. In arbitrary
  charts, inclusion (II) uses the dual action of the inverse gate (`(N⁻¹)ᵀ = N` for N-CLASS gates).
- **Six copies, no uniformity.** KT(6; 012|345, 03|1425, 14|25) gives three things:
  - the cross-triple relation `K₀₁₂ = T₃(K₃₄₅*)`, both inclusions, with closedness for (I);
  - SLOCC invariance of each triple cone;
  - the GHZ dichotomy, in the uniform form.

  The minimal hulls `M_bs`, `M_tw` and `M_odd` fail when both triples carry them.
- **The mixed pair (BS*, BS) on the two triples:**
  - It satisfies every six-copy family EQ3 derived.
  - The −1/16 witness `½ − GHZ` is not an effect of BS*'s side.
  - Through the four-token group (1,4,2,5)'s full effect set, the CNOT Choi effect `Ad(CNOT₁₂)(Ω₁₄ ⊗ Ω₂₅)`, if it is
    an effect of that group, excludes (BS*, BS) at −½.
  - With that effect, `Ad(CNOT)`-invariance of the triple cone (IE₂ for cnot) follows (audit U2, an exact identity).
- **No-generation lemma (EQ3, written).** Generation from pair-level data never produces a GHZ-class state.

## Coordinator's expectations (to be checked, never assumed)

**E1 — nine tokens force triple-level uniformity (Priority 1).**
- Setup: three mutually disjoint triples A, B, C. Join each pair of triples by Bell links under any matching; the
  cross pairs' native gates supply the links.
- Apply KT to the three six-token subfamilies A∪B, B∪C and A∪C, using both inclusions and closedness. This gives
  `K_A = T Π(K_B*)`, `K_B = T Π(K_C*)` and `K_A = T Π(K_C*)`, with Π the matching's relabeling (aligned charts, c = 0).
- **Expected consequences:**
  - each triple cone is invariant under permutations of its tokens, because any matching is allowed;
  - all three coincide up to relabeling;
  - the common cone is T-co-self-dual: `K = T(K*)` for c = 0, and `K = K*` for c = 1 with twin links.
- **Pigeonhole certificate (pre-checked exactly).** Any assignment of {BS, BS*} to three triples puts the same cone on
  two of them.
  - (BS, BS) fails (I3) at −1/16: the effects are `½ − GHZ` and GHZ.
  - (BS*, BS*) fails (II3) at −1/16: the states are `½ − GHZ` and GHZ, with Bell effects.
- **General form.** Three disjoint k-token groups (3k tokens) force k-level uniformity and co-self-duality.
- If E1 holds, uniform composition is derived, not assumed, at every level.

**E2 — crossing-constraint calculus (Priority 2).**
- For a crossing `(A|B, C|D)` with intersections `P = A∩C`, `Q = A∩D`, `R = B∩C`, `U = B∩D`, read `x_C` as a map from R
  to P and `y_D` as a map from U to Q (Choi–Jamiołkowski, with transposes). The constraint then says:
  `(Λ_x ⊗ Λ_y)(K_B*) ⊆ K_A` (closedness), for all `x ∈ K_C`, `y ∈ K_D`.
- With uniform co-self-dual cones:
  - `K_n ⊇ (id ⊗ Λ_y∘T)(K_{n−b+a})` for every `y ∈ K_{a+b}`, viewed as a map from a tokens to b tokens;
  - that is, maps whose transposed Choi operators are states of `K_{a+b}` act with idle extension.
- The audit's lever is the case n = 3, a = b = 2.

**E3 — the Choi lever is equivalent to the target (Priority 2).** Assume KT∞, the pair premises, closedness and full
effects. Then these are equivalent:
- (i) `K₃ = PSD₈` (c = 0);
- (ii) `K₃` contains a GHZ-class state;
- (iii) `K₄` contains the CNOT Choi state. By co-self-duality at k = 4, this is the same as the CNOT Choi effect being
  an effect of the four-token composite.
- (iv) `K₃` is invariant under the native gate acting on two of its tokens: IE₂ for the gate.

Witnesses, one for each direction used:
- (iv)⇒(ii): the gate on `|+⟩ ⊗ Φ⁺`.
- (ii)⇒(i): SLOCC invariance, closure and co-self-duality. That the GHZ class is a single dense orbit is Dür–Vidal–Cirac
  [L]. Density is the complement of the hyperdeterminant hypersurface.
- (i)⇒(iv): immediate.
- (iii)⇒(iv): the audit's U2 identity, via E2 with a = b = 2.
- (i)⇒(iii): via E2 with n = 4, a = 1, b = 2 and the copy factorization (pre-checked):
  `CNOT Choi = (V ⊗ id)(ψ₃)`, where V is the copy isometry, whose Choi state is GHZ, and
  `ψ₃ = Σ_ij |i⟩|i⊕j⟩|j⟩` is GHZ-class.

If E3 holds, the CNOT Choi effect is mathematically definable: it is `IsEffectOn` on any four-token cone inside PSD₁₆.
Its availability on the actual four-token composite, however, is equivalent to IE₂. So it cannot derive IE₂ unless it
is sourced independently.

## EQ4-P — research thread (Priorities 1 and 2): nodes, depth-first, decisive first, a verdict at each

**N1 — the mixed configuration (Priority 1).**
1. Verify E1 exactly, and in writing:
   - the three cross-triple relations, with arbitrary matchings;
   - the symmetry, uniformity and co-self-duality conclusions;
   - the pigeonhole certificate, re-derived in own code;
   - the c = 1 analogue;
   - the general-k statement.

   Handle charts: aligned first, then arbitrary token charts. Use the derived LU invariance of the triple cones, and
   the pair-level twist structure to fix the transposes.
2. Minimal instance, secondary and only if cheap. Does KT restricted to the six-token family alone already exclude
   (BS*, BS)? Here every subset of the six tokens carries a cone, with full effect sets, and all crossing constraints
   among them must hold.
   - An exclusion would come through the four-token group cones.
   - A survival needs an exact six-token model, with four-token cones that avoid both the CNOT Choi state and the
     effect.
   - Either answer fixes the smallest instance needed for uniformity. If neither is cheap, record the question as
     open.

**N2 — the Choi lever (Priority 2).**
1. Verify E2:
   - the general identity, as a written proof plus exact operator checks on six-token crossings, with random exact
     instances and symbolic where cheap;
   - the uniform corollary.
2. Verify E3, one direction at a time, with separately identified witnesses (§A.34).
3. **The owner's distinction.** State exactly what makes the CNOT Choi effect definable, and what its availability on
   the actual four-token composite is equivalent to.
4. Test whether any KT instance of any size, using only (s) and (2) steps, forces (iii). Extend the no-generation lemma
   to conditioning on effects of larger groups. Show whether such generation is circular, needing those groups' cones
   to already contain the relevant elements, or not.

**N3 — the reduced wall.** With E1 and E3, the wall is a classification of the fixed-point hierarchy `(K_n)`. Each
`K_n` must be:
- closed, convex, token-symmetric and SLOCC-invariant;
- co-self-dual (c = 0) or self-dual (c = 1);
- between the minimal and maximal composites;
- closed under the E2 Choi maps.

Decide it either way:
- **(a) an exact countermodel:** cones `(K₃, K₄, …)` with `K₃ ≠ PSD₈`, satisfying every constraint among the families
  of a stated finite size;
- **(b) a theorem route** to `K₃ = PSD₈`.

Also decide whether a c = 1 cone exists at all; if none exists, c = 1 is excluded by KT∞.

Tools:
- the GHZ-diagonal sector. There `K₃`'s sector is self-dual, because T acts trivially. It contains
  `cone{e_j + e_k}` and is invariant under the sector symmetry group and the dephasing semigroup induced by SLOCC.
  Exact polyhedral computations here give **necessary conditions only**.
- other symmetric sectors;
- explicit hierarchies;
- proofs.

Pressure-test every favourable branch.

**N4 — the missing principle, only if N3 does not close.** Test candidate additional principles A. For each:
- (a) is it state-level or operation-level?
- (b) does `P ∧ A ⇒ IE₂` hold, with a proof?
- (c) does `P ∧ IE₂ ⇒ A` hold? If both, A is the extension principle in disguise relative to P.
- (d) give an exact model of `P ∧ IE₂ ∧ ¬A`, if one exists. That shows A is strictly stronger.

Candidates, at least:
- **purification**, with "pure" meaning an extreme ray of the composite cone. Note that a purification of the
  classically correlated pair state is GHZ-class in QM. Check whether non-PSD extreme rays break this.
- **Choi availability of the native gate** (E3 predicts disguise);
- **transitivity of reversible dynamics on the pure states of composites** (operation-level).

Report which candidates are genuinely new principles and which are IE₂ restated.

**N5 — literature (cheap; egress may be blocked).** Mark everything not read at the source [L, unverified]. Targets:
- Gühne–Seevinck (GHZ-diagonal biseparability);
- Dür–Vidal–Cirac (three-qubit SLOCC classes);
- Chiribella–D'Ariano–Perinotti (purification);
- Barnum–Wilce and Barnum–Graydon–Wilce (composites);
- Müller–Ududec (bit symmetry).

### Productivity test (fixed before the walk)

A finding is a **gem** iff it is one of:
1. an exact certificate deciding Priority 1 at a stated instance;
2. a theorem route, every step checked, for a stated equivalence of E3 or for a closure of the wall;
3. an exact countermodel at a stated finite instance with `K₃ ≠ PSD₈`;
4. an exposed hidden assumption;
5. a classification of a candidate principle as disguised IE₂, or as strictly new, with the required proof and model.

Otherwise it is record-only. Results are stated for the instance actually used, never for "KT∞" in general unless
proved for all instances.

### Deliverable (EQ4-P)

`scratchpad/eq4/P/RESULT.md`, plus a running `NOTES.md` and the scripts. It opens with **0. Answer to the decisive
question**: positive, negative or open, with the precise instance and the named wall.

Then come EQ3's sections:
- Finding
- Target theorems (UNBUILT)
- Hypotheses ledger, with independence evidence under the P/A/C rule
- Missing lemmas
- Formalization strategy
- Research questions
- Evidence and probe log

Classify the outcome in the owner's five-way table, for IE₂.

## EQ4-F — formalization package thread (Priority 3)

**Goal:** package KT(4; 01|23, 02|13) → IE₁ as a precise, reviewable result, with every premise explicit. Keep it
separate from claims of necessity, and from any suggestion that KT(4) follows from the certified base.

**Deliverable:** `scratchpad/eq4/F/FORMAL.md`, plus UNBUILT Lean text in `scratchpad/eq4/F/`.

1. **The theorem package.** Statements:
   - the forward theorem: pair classification, IE₁ and parity;
   - the aligned form;
   - the general-chart form;
   - the closure-level form, which needs no closedness.

   Every hypothesis is a named predicate:
   - the two-grouping coherence (H-KT4);
   - closedness (H-closed);
   - the native gate and its inverse as standalone operations (H-gate, H-inv);
   - N-CLASS, for general charts only;
   - admissibility and convexity (H-adm);
   - local tomography of the regrouped composites (H-LT);
   - every pair carrying the two-copy premises (H-pairwise);
   - the full `IsEffectOn` effect quantifier (H-eff).

   Mark each hypothesis [K] landed (with file:line), transported, or unsourced.
2. **Proof skeleton.** Map every step to its evidence: EQ3 and audit script check ids, and [W] steps. Tag each step (s)
   or (2).
3. **Lean design (UNBUILT), in base vocabulary.** The base has: `W 3`, `cnot`, `phiW`, `prodState`, `pairVal`,
   `CandidateCone`, `IsEffectOn`, and COMP-1's `PreComposite` and `Composite`. Read names and signatures at the base.
   Prefer an interface that takes the two inequality families as the hypothesis `FourCopyCoherent K01 K23 K02 K13`.
   That needs no four-copy carrier. State separately the lemma deriving the families from a COMP-1 four-copy composite;
   that one needs new carrier vocabulary. Split the work:
   - cheap real-linear-algebra parts: the inclusions from the families, `Δ·f·Δ = T f`, orthogonality of N-CLASS gates;
   - heavy parts: the Pauli dictionary over ℂ, link filters, density and closure, the spectral theorem.

   Name every Mathlib fact needed, and check that it exists in the local snapshot `scratchpad/ml-v433-src/m` (tag
   v4.33.0) by grep only. Mark "not found" honestly.
4. **Scope statements, in the package itself:**
   - what is not claimed: necessity, any base derivation of KT(4), anything at three copies;
   - the converse equivalence under uniform composition (`KT(4) ⟺ IE₁`, audit §4) only as a separately labelled
     remark, with its own witness. It is not part of the package's theorem.
5. **Proposed rounds and costs.** Not frozen. Include a recommendation, for the owner to decide, on whether to run a
   kernel design check on a disposable branch. This thread does not run one.

## Limits (both threads)

These are EQ3's limits, with these changes:
- **Writes:** EQ4-P writes only inside `scratchpad/eq4/P/`, and EQ4-F only inside `scratchpad/eq4/F/`.
- **Reads:** you may read `scratchpad/eq2/*`, `scratchpad/eq3/*`, `scratchpad/eqreview/*`, the base at
  `scratchpad/eq/base/`, and the local Mathlib snapshot (grep only). Never modify any of them.
- **Arithmetic and evidence:**
  - Exact arithmetic only for anything certified.
  - Floating-point runs are exploration, labelled in the filename and header, and never cited as evidence.
  - Every verdict prints only over green controls, with a countercontrol for every favourable branch (§A.21, §A.31).
- **Scripts** run as `python3 -I -B`, with byte-identical replays recorded.
- **No outward actions:** no git writes, branches, pushes, PRs, CI, freezes, ROADMAP or manuscript edits, or premise
  adoption. Do not spawn agents. No Lean toolchain is available, so all Lean text is UNBUILT.
- **Integrity:** check the base manifest at the start and at the end (`cd scratchpad/eq/base && sha256sum -c --quiet
  ../base.manifest.sha256`). Check that the repository is clean at HEAD `bc3bf9bc`. Record a start marker.
