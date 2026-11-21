# OIQM-UNBOUNDED: one scalable exact OI model across finite carrier sizes (P1 link O2)

**Standing.** WIP / UNVERIFIED author record of a paper-only gem-finding unit (§A.31, depth-first). It has
not been independently reviewed. It proves nothing in Lean, runs no computation, edits no manuscript and
changes no status. Base: `origin/main` at `df6da1c6`. `Main:n` and `GR:n` are lines of `papers/*.md` at that
base. Lean identifiers are in `verification/lean-mathlib/OIBridge/`. Issue #1500; thread #1169.

**Scope set by the owner** (#1169 c.6876591512 answer 3; c.7064859041). The target is one coherent,
scalable construction that accommodates arbitrarily large finite carriers, with compatible dynamics and
observation interfaces across sizes. A family of separate per-size models does not meet it. The explicit
test is compatibility: embeddings between sizes, restriction of the dynamics along them, and observation
interfaces that commute with both.

**Dependency.** The A1 retirement (#1477) is pending. Nothing here treats it as landed, and nothing assumes
that it would establish the existence or consistency of an infinite OI system. §6 lists the steps that
would need it.

**Labels** (#1169 c.7064843184). **(N)**: proved from OI's native assumptions, which are the substratum
premises of the posit ledger (Main:736) together with mathematics. **(I)**: conditional on imported quantum
or operational assumptions, each of them named. An imported *mathematical* theorem (for example a
nonnegative-rank bound) does not make a result (I). An imported *physical or operational* premise does.

## 0. Productivity test, fixed before the walk

The unit is a **gem** if it yields at least one of the following:

- (a) a necessary condition on every single exact model, provably stronger than the fixed-finite-carrier
  obstruction (Main:568);
- (b) a reduction of O2 to a strictly smaller, named question;
- (c) an exposed hidden assumption in an existing record or theorem.

A merge of kernel results into one table is a **non-gem**, and so is relabelling. Both would be
record-only. Any favourable branch gets maximum skepticism at its own node.

## 1. Node 1: where finiteness enters the existing results

| Result | Finiteness hypotheses | Load-bearing? |
|---|---|---|
| L0 `finite_horizon_equivalence` (Equivalence.lean:462) | `Fintype V`, finite horizon `K`, `Fintype` hidden carrier and basis | `exists_perm_extending` uses finiteness in its proof: an injective partial map on an infinite type need not extend to a permutation (take `succ` on `ℕ`). On the finite domain `coh V K` the construction is unaffected by the size of an outer carrier. `Qfb_imp_S` uses finite sums; with an infinite basis, ℓ² columns would serve. The class is per-horizon and per-law, so it has no bearing on a single model. |
| L3 `exactAll_iff_physical_general` (GeneralCarrier.lean:100), L4 `carrier_general_oiPlus` (CarrierGeneralOIPlus.lean:213) | `[Fintype A] [Nonempty A]`; ancilla levels `A × Fin n` with finite `n`; finite outcome types; finite Kraus families | Yes, every carrier is finite. **But one theory covers every level:** `FiniteOperationalTheory A` (OperationalAssembly.lean:594) carries `availExt n` for every `n : ℕ`, and `ExactCompositeQuantumOps` (AncillaClosure.lean:364) quantifies over every `k`. See Node 2. |
| L5 `substratumGen_not_control` (StructuralClosure.lean:330) | `Fin 2` only | Witness scope only. |
| L2 finite-substratum obstruction (Main:568) | `N < ∞` ontic configurations | The whole content of the result. An infinite ontic carrier escapes it. See Node 4. |
| L7 region completion (`QuasilocalCharacterization.lean`, `QuasilocalAlgebra.lean`, `RegionTower.lean`) | sites `ι` arbitrary, possibly infinite; `[Fintype Q]`; regions are `Finset ι` | Each stage is finite. The tower is the only infinite object, and `ReversibleDynamics` (QuasilocalAlgebra.lean:956) is a bijection of `ι → Q` with finite dependence and finite influence. |
| `q3_countermodel` (InstrumentAvailability.lean:335) | `[Infinite ι] [Nontrivial Q]` | Uses infinitude to exhibit an operation (the all-sites phase) that no finite-support availability reaches. |
| Main:650 consolidation | finite bijection, so finite order `L` | Exact periodicity is a finite-carrier fact. It is lost on an infinite carrier (Node 5). |

**Verdict N1.** Finiteness is load-bearing in two places only: the size of each operational level (L3/L4)
and the ontic carrier (L2, Main:650). Every other use is scope.

## 2. Node 2: is one operational object over all finite sizes already typed?

**Claim 2.1 (established, kernel; label (I)).** A single `T : FiniteOperationalTheory A` with
`ExactAllFiniteEndomorphicQuantumOps T` is exact finite operational QM on `A × Fin (k+1)` for **every**
`k`, by the definition `ExactCompositeQuantumOps` (AncillaClosure.lean:364). Any finite carrier `B` with
`|B| = |A|(k+1)` is reached along a bijection, and the Kraus form is invariant under it in both directions
(`isKraus_transport`, LevelOneSeam.lean:170).

- **Compatibility.** Inclusion of a smaller level into a larger one, acting as the identity on the added
  factor, is condition (iii) `InertSpectatorCompositionality` (SpectatorBridge.lean:223). Using a level as
  the base of a larger experiment is condition (v) `IteratedAncillaClosure` (AncillaClosure.lean:247). So
  at the operational layer, the owner's compatibility test is exactly two of the five conditions. Both are
  proved necessary for exactness (`physical_of_exactAll`), and on the qubit each of them has a witness theory
  satisfying the other four conditions without it (`five_way_minimality`, qubit-scoped).
- **Imported.** Complex matrix kinematics, as Main:572 states. Under `qm_of_oiPlus` the conditions are
  supplied by the OI⁺ principles, so they are posited, not derived.

**Skepticism at this node (the branch is favourable).**

- (i) **Witnesses on every carrier.** The kernel has an exact theory on every nonempty finite `A`,
  `Fin 1` included. `fullClass_quantumArchitecture` (SubstratumSource.lean:151) with
  `genTheory_qm_of_quantumArchitecture` (SubstratumSource.lean:136) gives `ExactAllFiniteEndomorphicQuantumOps`
  of `genTheory fullClass _ A`. `substratum_plus_control_qm` (StructuralClosure.lean:397) is a second route.
  Composed with `physical_of_exactAll`, either gives joint satisfiability of the five conditions on every
  carrier. On `Fin 1` this is one theory exact at every finite size. Its exactness comes from the full class
  of operations, so it is (I). Only the witness instantiated inside `main_result` (ii) (`fullQuantum`) and
  `five_way_minimality` are qubit-scoped. The witnesses `fullQuantum`, `pairFlowTheory` and `mixTheory` are
  qubit-only. One caveat on compatibility: inert spectators reach only levels `m` with `|R|·n = m`.
- (ii) **The object is not a model.** `FiniteOperationalTheory` is a family of availability predicates. It
  has no ontic carrier, no dynamics and no probability `p_M`. Target I needs a substratum–observer
  realization with law equality, and the only link to OI (`RealizesSealedOICore`, OIRealization.lean:234)
  is to one fixed four-level core on `Fin 2`.

**Verdict N2.** CONFIRMING. A single operational object over every finite size already exists in the
kernel, as (I). O2 is therefore not an operational-typing problem. It is a **realization** problem: one
ontic construction whose observer-level theory is such a `T`. The walk continues there.

## 3. Node 3: candidate constructions, under the compatibility test

The test has four parts:

- **(T1) embeddings** compose along a directed system of sizes;
- **(T2) dynamics** is carried along the embeddings;
- **(T3) the observation interface** (readout, availability) commutes with embeddings and dynamics;
- **(T4) states and priors** restrict consistently.

**3A. The tower of periodic finite tori, under divisibility.**

- *Embedding.* `ι_{L,L'}`, for `L | L'`, sends a configuration of the torus `(ℤ/L)^d` to its `L'`-periodic
  lift. The lift is injective.
- *Dynamics, (T1)–(T2) pass.* The lift intertwines exactly with any translation-covariant finite-range
  rule whose radius is below `L`. Periodic lifts are invariant under the rule's own update, so (T2) holds
  with equality: the dynamics restricts.
- *Priors, (T4) holds only as conditioning.* The counting measure on `(ℤ/L')^d` (ledger item (iv))
  assigns the image of `ι_{L,L'}` the weight `|Q|^{L^d − L'^d}`, which tends to 0 as `L'` grows. The
  image is invariant under the dynamics, and the conditional of the counting measure on it is the
  counting measure of the small torus. So priors are compatible, but only as conditionals on a sector of
  vanishing weight, which a generic configuration of the large torus does not occupy.
- *Observables, (T3) fails at scale.* The induced algebra map `M_{C_L} → M_{C_{L'}}` is a non-unital
  corner map. An observer region of diameter below `L` sees the same marginals in both models. A larger
  region sees correlations that periodicity forces and the large model's counting prior does not. So the
  observation interface commutes with the embeddings only for observers smaller than the smallest torus,
  which is uniformly false along a tower meant for arbitrarily large carriers.
- *Recurrence.* The exact recurrence index `L` of Main:650 is not preserved along the tower.
- **Verdict 3A (paper, (N)).** Compatible in its dynamics. Compatible in its priors only by conditioning
  on vanishing-weight sectors. Incompatible in observation at scale. As a scalable construction it fails
  (T3), and is in effect a family of per-size models.

**3B. The region tower over an infinite lattice** (the Level III object, GR:279–294).

- (T1) holds: `inclObs_trans` (RegionTower.lean:152).
- (T2) holds in cone form only. The dynamics is not an endomorphism of any stage. It carries a stage
  observable of `Λ` to one of the `k`-fold hat region (`heis_iterate_emb`, QuasilocalAlgebra.lean:1330),
  and extends to an automorphism `heisQ`. "Restriction of dynamics" is therefore replaced by its causal-cone
  form. A literal restriction to a finite region exists only for dynamics that decouple the region.
- (T4) holds: `quasiState_unique` (QuasilocalAlgebra.lean:879). The uniform family is consistent
  (`uniform_family_consistent`, RegionTower.lean:447). On the ontic side this is the uniform Bernoulli
  measure on `Q^ι`, whose marginals are the counting measures of every region. So the region tower, unlike
  3A, does carry the counting selection (item (iv)) consistently across sizes.
- (T3), the algebra and the canonical isomorphism, hold: `quasilocal_characterization`
  (QuasilocalCharacterization.lean:856), with the dynamics `systemEquiv_dyn`. This is a **uniqueness and
  isomorphism** theorem. Per §A.34 it is not an equivalence, and it derives no OI_Q condition from the
  existence of a quasilocal system.
- (T3), the operational interface: the kernel has the fixed-carrier predicate `AvailFS`
  (InstrumentAvailability.lean:168). It is closed under the OI dynamics (`availFS_dyn`, :218) and is
  **defined** to contain every finite-region Kraus instrument (`availFS_of_kraus`, :237;
  `kraus_of_availFS`, :242). Its quantum content is posited. The GR text says the same: OI_Q is "the
  current OI substratum together with continuous off-diagonal controllability" (GR:284).
- **Verdict 3B.** All four compatibility parts hold, where (T2) holds in cone form. The algebra, states and
  dynamics are (N) as mathematics: matrix algebras on configuration spaces, with permutation dynamics. The
  reading of the full stage algebra as the observer's operational algebra is **(I)**. It imports continuous
  off-diagonal controllability, which is O1, together with complex kinematics.
- **3B is the natural scalable candidate.**

**3C. Encodings of arbitrary finite carriers in 3B** (standard mathematics; Glimm's classification of UHF
algebras).

- **Unital encodings.** A unital `*`-homomorphism `M_d → M_m` exists iff `d | m`, since the multiplicity
  must be an integer. A carrier of dimension `d` therefore embeds unitally into some stage, compatibly with
  the tower inclusions `X ↦ X ⊗ 1`, iff every prime factor of `d` divides `|Q|`. The quasilocal algebra is
  the UHF algebra of supernatural number `|Q|^∞` when `ι` is countably infinite. An uncountable `ι` gives
  a non-separable algebra.
- **Corner encodings.** For the `q = 2` model of Main §3.2, a carrier of dimension 3 has no unital encoding
  on any region. It enters only as a corner `p M_{2^k} p`.
- **Corner lemma (paper; (I), since it assumes stage exactness).** If the stage theory is exact QM, then
  the corner theory is exact QM. For soundness, an instrument on the stage that preserves the corner
  compresses to a valid instrument. For completeness, `K_1 ⊕ (1 − p)` together with `K_i ⊕ 0` for `i > 1`
  is a normalized stage Kraus family.
- So the restriction to powers of `|Q|` costs nothing once the stages are exact. The price is that every
  such carrier comes with a **stated encoding** (the projection `p`), and its operations must be
  leakage-free, which is answer (c)3's "stated encodings".

## 4. Node 4: the decisive branch, exactness on an infinite ontic carrier

L2 forbids a fixed finite ontic carrier. The ontic carrier of 3B, `Q^ι` for infinite `ι`, is uncountable,
so L2 does not apply to it. The favourable reading is that the infinite lattice escapes the obstruction.
Maximum skepticism goes here.

**4.1. Measurable structure gives no obstruction (remark; sketch; (I)).** For countably infinite `ι` and
`|Q| ≥ 2`, `(Q^ι, product σ-algebra)` is an uncountable standard Borel space. By Kuratowski's theorem it is
Borel-isomorphic to every other uncountable standard Borel space, among them the ontic spaces of
ψ-ontic ontological models of `d`-level QM (the ψ-complete Beltrametti–Bugajski model; the Kochen–Specker
qubit model, which is ψ-supplemented, not ψ-complete, in Harrigan–Spekkens' classification) and their disjoint union over `d`.

- *Import.* This uses the Hilbert-space state itself as the ontic variable.
- *Named gap.* Making such a model *deterministic and reversible* with collapse needs an infinite padding
  step: a Borel extension of an injective partial map to a bijection. Finite padding (L0's
  `exists_perm_extending`) is the step that fails on infinite types (Node 1). That step is not done here.
- *Role.* The remark shows that measurable size alone is no obstacle. **Any** obstruction to O2 on the
  lattice must use structure beyond the measurable: site factorization (ledger (viii)), finite range ((ix),
  A3) or native operations. The relabelling destroys all three.

**4.2. Proposition U (unbounded readout cone; paper proof; label (I): it imports preparation–setting
independence, ledger item (xiv), beyond its stated Bell scope, and the mathematical theorem [55]).**

*Setting.* The ontic space is `Ω = Q^ι`, site-factorized (viii). A *native measurement* consists of:

- a preparation, which may be **any** probability measure `μ` on `Ω`;
- a finite sequence of `ReversibleDynamics` steps (dynamics or interventions, each with finite dependence
  and finite influence);
- an outcome that is a function of the configurations of one finite visible region `V` at the steps of the
  sequence. `V` is finite by the finite-capacity clause, Lemma 1.

The *readout cone* of the measurement is the finite region `R` on which, by iterated finite dependence, the
outcome depends at time 0. This is the ontic counterpart of `heis_iterate_emb`.

*Claim.* Let `𝓜` be any set of native measurements whose readout cones all lie in one finite region `R`.
Then every prepare-and-measure behaviour matrix over any preparations and over measurements in `𝓜`
factors through the `|Q|^{|R|}` configurations of `R`. Hence its nonnegative rank is at most `|Q|^{|R|}`.
Therefore, if one model on `Ω` reproduces exactly the prepare-and-measure behaviour of even one qubit, the
union of the readout cones over its measurement set lies in no finite region. With a bounded-degree graph
and a finite catalogue of radius-`r` rules (A3), the cones lie in `B(V, rK)`, and the measurement depth `K`
is unbounded over the measurement set.

*Proof.*

- **Where (xiv) enters.** The preparation law `μ` is taken to be the same whichever measurement in `𝓜`
  follows it, so `B(p, m) = ∫ ξ_m dμ_p`. On a native substratum the setting is itself a configuration, so
  this is setting independence, ledger item (xiv). Main:736 scopes (xiv) to the Bell analysis of §3.3. It
  is the "ordinary preparation → ontic system → measurement" interface that Main:568 names as assumed.
- The probability of outcome `o` is `μ(f_o ∘ π_R) = (π_R μ)(f_o)`. The response depends on `x` only through
  `x|_R`, so `B = Ξ_R · (π_R M)`, with `Ξ_R` having entries in `[0,1]` and `π_R M` column-stochastic over
  `Q^R`.
- This is the factorization interface of Main:568 with `N = |Q|^{|R|}`.
- For the qubit, the nonnegative rank of prepare-and-measure behaviours is unbounded over finite
  prepare–measure sets (Heinosaari–Kerppo–Leppäjärvi–Plávala, Main [55]).
- So no finite `R` serves every finite qubit experiment. The bound `R ⊆ B(V, rK)` is the causal cone of
  A3. ∎

*Classification.*

- **Native premises used:** (viii), the `ReversibleDynamics` finite-range structure, (ix)/A3 for the depth
  form, and Lemma 1's finite visible region. Item (xiv) is not native in this
  scope; see Imported.
- **Imported:** preparation–setting independence, (xiv), used outside the Bell scope that Main:736 gives
  it. This is an operational premise, so the label is (I). The theorem [55] is imported mathematics. The
  quantum behaviour is the comparison target, not a premise. The same use of (xiv) outside its scope is
  flagged by BQ1's AW-1 (#1498).
- **Layer:** paper (P). Not in the kernel.

*Skepticism, loophole by loophole.*

- (a) Preparations are unrestricted, so no preparation choice evades the bound.
- (b) If interventions are arbitrary bijections, as in the gluing theorem (Main:574–592), the bound fails.
  For the observer as a native part of the substratum, its actions are substratum dynamics, so the bound
  applies. *Assumption-watch AW-U1:* any O2 construction that lets observer interventions be non-finite-range
  bijections is non-native, and is (I) on that point.
- (c) The proposition does **not** forbid exactness. Each finite experiment has a finite cone, and the cone
  may grow without bound. It forbids exactness with a uniformly bounded readout cone.
- (d) Intermediate and adaptive readouts at `V` are included, because their joint outcome is still a
  function of `x|_R`.

*Is it stronger than the restatement?*

- **Only as a corollary.** Mathematically, U is L2 applied to the pushforward `π_R μ`, a one-step
  corollary. As a necessary condition it is not provably stronger than L2, so criterion (a) is borderline.
  What it adds is its reading on an infinite carrier: a native exact qubit cannot be read within any fixed
  finite region of the substratum.
- **Consequence for 3B (exposed hidden assumption).** In 3B a carrier is a *finite-region stage*, and its
  sharp effects are elements of that stage. By Proposition U, a native realization of the stage's sharp
  effects cannot have finite-region ontic response.
- So the identification "finite carrier ↔ finite region" holds in the quantum completion and **fails at
  the ontic level** for every native exact realization that satisfies (xiv). The region tower's (T3) therefore cannot be
  realized natively with exact laws by region-local readouts. Any native O2 construction must use readout
  cones that grow with the resolution demanded.
- *Assumption-watch AW-U2:* "the carrier lives on a finite region" is exact only in OI_Q (I). Ontically it
  is at best quasilocal, as a limit over growing cones.

**Classification of the node.** ELABORATING, as a corollary of L2. Its gem content is AW-U2, under
criterion (c). Under (xiv) it fixes what a native single model must do (unbounded readout cones), and it
rules out every bounded-readout scalable construction. Its preparations are arbitrary measures, more
generous than O3's native preparation, so it is a necessary condition only. Negative scope: it applies to the class stated, native
finite-range readouts on a site-factorized carrier, and to no wider class.

## 5. Node 5: infinite carriers and the inequivalence issue (literature, Step 4)

- **Inductive limits.** A direct limit of full matrix algebras with unital connecting maps is a UHF
  algebra, classified by its supernatural number (Glimm 1960). With general maps it is an AF algebra
  (Bratteli 1972). The 3B completion is the UHF algebra `|Q|^∞`. The kernel's `canonEquiv` and
  `systemEquiv` are its universal property, specialised to the tower of region stages.
- **Infinite tensor products and sectors.** Von Neumann's complete infinite tensor product splits into
  incomplete products, which are mutually orthogonal sectors. The quasilocal algebra has uncountably many
  inequivalent irreducible representations, and product states yield factors of every type (Powers 1967;
  Araki–Woods 1968).
- *Classical counterpart on the ontic side.* Product measures on `Q^ι` whose site marginals differ at
  infinitely many sites, enough to violate Kakutani's criterion, are mutually singular (Kakutani 1948).
- *Bearing on O2.* None, for finite carriers. A finite carrier lives on a finite stage, `M_n` has one
  irreducible representation, and a finite-support quantum operation stays in the same sector. On the
  ontic side, a finite-support bijection keeps a product measure with full-support site marginals, such
  as uniform Bernoulli, absolutely continuous. Without full support this fails: a point mass with one
  site flipped is singular to the original. This matches GR:292 and `state_selection_audit`: no
  representation is selected, and a sector is an initial-condition input.
- *Bearing on an infinite carrier* (an infinite subsystem as the working system): one model cannot connect
  states in different sectors by any finite-support operation, and `q3_countermodel` shows that
  infinite-support coherent operations are not entailed. **So "one exact model covering an infinite
  carrier" is sector-relative in principle:** at most one sector per initial condition.
- **Verdict:** ELABORATING. The literature confirms the kernel's scope and adds the sector restriction as
  standard.
- **Recurrence on an infinite carrier (a question for the owner, not a result).** Axiom 2 (Main:36) says
  that differentiation recurs. It is not exact orbit return. The exact finite-index return and its index
  (Main:650) are finite-representative statements under ledger item (ii) (Main:736). Known mathematics
  bears on that return on 3B:
  - with countable `ι`, a surjective CA preserves the uniform Bernoulli measure (Hedlund 1969 for `d = 1`),
    so Poincaré recurrence holds almost everywhere;
  - a CA with `Φ^n = id` (finite order) returns exactly everywhere;
  - spatially periodic configurations return exactly, but they form a null set.

  So exact finite-index return is not guaranteed on 3B unless `Φ` has finite order.
  *Question for the owner:* which form of return, if any, a statement about 3B must keep.
  *Assumption-watch AW-U3:* a result that consumes the exact finite-index return of Main:650 (item (ii)
  uses) transfers to 3B only for finite-order `Φ`, or in an almost-everywhere form.

## 6. The A1 dependency, step by step

| Step | Needs the A1 retirement? |
|---|---|
| Nodes 1–2, 3A, 3C, Proposition U as a no-go | No. They are mathematics about stated classes. Proposition U is a no-go over the stated infinite class and asserts the existence of no OI model. |
| Asserting that the OI substratum *is* 3B (an infinite `Q^{ℤ^d}` with uniform Bernoulli prior) | Yes, and more besides. The retirement would remove the finiteness posit. It would not supply the following, and none of them is assumed: exact finite-index return on 3B (Main:650; not guaranteed unless `Φ` has finite order, AW-U3); Lemma 3's injectivity recovery, which closes its margin on a finite representative (Main:736 (iii)); and the counting-measure selection (iv), replaced by the Bernoulli family, which needs its own justification. |
| Any manuscript or registry statement of the above | Yes, and it is frozen material (Main:590, :650, :712, :730; ledger item (ii)). None is proposed. |

## 7. The owner's three questions

**Established.**

1. *(Kernel, (I).)* One operational object exact on every finite level `A × Fin (k+1)`. The compatibility
   test at that layer is conditions (iii) and (v). Witnesses exist on every nonempty finite carrier,
   `Fin 1` included (`fullClass_quantumArchitecture`, `genTheory_qm_of_quantumArchitecture`). Only
   `main_result` (ii) and `five_way_minimality` are qubit-scoped (Node 2).
2. *(Kernel, algebra and dynamics (N) as mathematics; operational reading (I).)* The region tower passes
   (T1)–(T4), with (T2) in causal-cone form. Its uniqueness theorem is not an equivalence (§A.34) (Node 3B).
3. *(Paper, (N).)* The periodic-torus tower is dynamically compatible, meets the prior test only by
   conditioning on vanishing-weight sectors, and fails the observation test at scale (3A).
4. *(Standard mathematics.)* Unital encoding iff the prime factors of `d` divide `|Q|`, otherwise a corner
   encoding. *(Paper, (I).)* The corner lemma (3C).
5. *(Paper, (I): imports preparation–setting independence (xiv) beyond its Bell scope; mathematical
   theorem [55].)* **Proposition U**, a corollary of L2: a native exact qubit on a
   site-factorized finite-range substratum needs readout cones that lie in no finite region. Hence the
   finite-region carrier of 3B is not natively realizable with exact laws by bounded readouts (Node 4.2).

**Assumed** (where it enters).

- Complex matrix kinematics: Node 2, 3B, 3C. This is Lean structure, `Matrix A A ℂ` in
  `FiniteOperationalTheory`.
- Continuous off-diagonal controllability, or OI⁺, as the source of exactness on stages: 3B (T3) and the
  corner lemma. In Lean: `HasCompositeUnitaryControl`, and `AvailFS` defined to contain every Kraus
  instrument.
- Inert spectators and iterated closure as the operational compatibility rules: Node 2. In Lean:
  `InertSpectatorCompositionality`, `IteratedAncillaClosure`.
- An infinite site set: 3B, Node 4. In Lean: `[Infinite ι]` in `q3_countermodel`. It is not adopted.
- Preparation–setting independence, ledger (xiv), beyond its Bell scope: Proposition U, at the
  factorization `B(p, m) = ∫ ξ_m dμ_p` (Node 4.2).
- Imported mathematics: [55] (Proposition U), and Kuratowski, Glimm, Kakutani and Hedlund (remarks).

**Missing.**

- **The earliest unsupported step is (T3) on the scalable candidate 3B:** a *native* observation interface
  on the region tower whose available operations are exact on every stage. It needs a **physical
  mechanism**, namely O1 (a sourced non-monomial coherent operation). Under (xiv), Proposition U says it also needs a
  readout mechanism whose cone grows with resolution: an amplification-type process of unbounded depth.
  This agrees with BQ1 (#1498, reviewed at `3269772a`), whose H5 assumes a polynomial dependency cone.
  Polynomial cones are unbounded, so the two do not conflict. It agrees with QOPS (#1501, under revision),
  which places O1's earliest links at KIN (imported), then FLOW. The readout requirement is O3-type and
  conditional on QOPS's RES.
- **Mathematics still open:**
  - the infinite padding step of 4.1;
  - H-∞ (ROADMAP:81);
  - which form of return a statement about 3B keeps (AW-U3). This is a question for the owner; the
    relevant mathematics is known.

**Productivity verdict.** Gem under criterion (c) only: AW-U2, under (xiv). Criterion (a) is borderline,
because Proposition U is an L2 corollary. Node 4.2 is classified ELABORATING, Node 2 CONFIRMING, 3A, 3C and Node 5 ELABORATING. The fixed point is not
reached: one pass.

## 8. Preregistration (not run; computation is not authorized)

**PR-U1: minimal readout cone for an exact `N`-setting qubit experiment.**

- *Question.* For the equatorial qubit prepare-measure matrix with `N` settings, what lower bound on the
  nonnegative rank holds exactly? Hence, what is the minimal `|R|` with `|Q|^{|R|} ≥` that bound, and the
  minimal depth `K` on the `q = 2` cubic lattice with radius 1?
- *Decision rule.* Report the exact combinatorial lower bound (fooling-set or rectangle-covering) as a
  function of `N`. Derive `K_min(N)` from `|B(V, K)|` with no fitting. The verdict is generated from the
  measurements.
- *Controls.*
  - Positive: matrices of known nonnegative rank, such as identity matrices and the regular `n`-gon slack
    matrices, whose extension complexity is known to be `Θ(log n)`. The control fails if the bound
    misreports any of them.
  - Negative: a classical simplex model with `|Q|^{|R|}` states must reproduce its own behaviour at the
    computed `K`.
- *Scope.* It quantifies Proposition U. It does not decide O2.

## Sources (external)

Heinosaari, Kerppo, Leppäjärvi, Plávala, Phys. Rev. A 109, 032627 (2024) (Main [55]); Hardy, "Quantum
ontological excess baggage", Stud. Hist. Phil. Mod. Phys. 35 (2004); Montina, Phys. Rev. A 77, 022104
(2008), and arXiv:1002.3139 (its bound needs Markovian dynamics on a manifold and is not invariant under
Borel isomorphism, which is why it is not used here); Glimm, Trans. AMS 95 (1960); Bratteli, Trans. AMS
171 (1972); von Neumann, Compositio Math. 6 (1939); Powers, Ann. Math. 86 (1967); Araki and Woods, Publ. RIMS 4 (1968); Kakutani, Ann. Math. 49 (1948); Hedlund, Math. Systems Theory 3
(1969); Beltrametti and Bugajski, J. Phys. A 28 (1995); Harrigan and Spekkens, Found. Phys. 40 (2010).
