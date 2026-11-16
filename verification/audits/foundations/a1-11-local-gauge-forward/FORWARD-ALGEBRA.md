# A1-11 — A1-free forward local gauge algebra (A1-C04)

**Status:** AUTHOR DRAFT — paper-only source/proof assembly; not an adopted theorem or an independent review.  
**Accountable issue:** [#1336](https://github.com/amaybaum/incompleteness/issues/1336); coordination [#1169](https://github.com/amaybaum/incompleteness/issues/1169); distinct related scopes [#1211](https://github.com/amaybaum/incompleteness/issues/1211), [#983](https://github.com/amaybaum/incompleteness/issues/983).  
**Owner authority:** [activation c.6918441539](https://github.com/amaybaum/incompleteness/issues/1336#issuecomment-6918441539); [“Proceed here” / A1-11-only ChatGPT writer c.6919398063](https://github.com/amaybaum/incompleteness/issues/1336#issuecomment-6919398063). Earlier Codex-only planning and handoff are historical, not concurrent work.  
**Source pin:** `main` at `6eac91ee25a1afaea4ed148b0c54967a08b12ac3`, 2026-11-16. All `file:lines` references below are to that SHA unless noted; source links are at the end.  
**Scope:** standalone *forward mathematical* implication on supplied local data. No new theorem, physical premise, Lean, simulation, manuscript change or merge. No claim of an actual A1-free physical gauge realization.

## 1. Disposition and strongest defensible claim

**EXISTING CONDITIONAL ALGEBRA (A1-independent as a mathematical implication):** The six signed link directions of a specified three-dimensional simple-cubic local graph have an exact `3 ⊕ 2 ⊕ 1` cubic representation. **If** this representation is supplied as a *single-copy complex Hermitian observer/gauge carrier* (H-link, `m=1`), the pre-condensate kinetic structure is custodially scalar (H-cust), and a generic equivariant Hermitian condensate with distinct three block eigenvalues is supplied, its full unitary stabilizer is `U(3) × U(2) × U(1)`. Its Lie algebra is `u(3) ⊕ u(2) ⊕ u(1)`, **not automatically** the Standard-Model Lie algebra. A *specified* correlated two-torus quotient or a separately *specified* charged family and Higgs action produces an abstract/faithful group isomorphic to `(SU(3) × SU(2) × U(1))/Z₆ ≅ S(U(3) × U(2))`, whose Lie algebra is `su(3) ⊕ su(2) ⊕ u(1)`. The chosen chiral five-multiplet family, anomaly conditions and nonzero-quark-charge branch then give the usual hypercharge ratios, up to normalization and exchange of the two quark singlets. None of these conditional **local** conclusions needs finiteness of the total substratum.

This is an assembly of **already stated** implications in [MATRIX] L21–40, [SM] L340–382, L523–529, L575–599, [GLOBAL], [NATIVE] and [HYPER]. It does **not** assert that the optional quotient is selected by OI, that its required charged action is native, or that the resulting algebra is realized by gauge fields. The six-link projection is Lean-kernel-backed; the stabilizer, correlated quotient, charged action and anomaly classification have existing *paper/written algebra* support, not a new Lean certificate. Substratum Theorem 23 ([SUB] L193–205) is a stronger, A1-assuming **reconstruction** statement; it is not the premise of this restricted forward implication.

### Explicit assumptions → conclusions (one composite *conditional* statement)

Fix the following named data, rather than deriving or selecting them from observational outcomes:

- **L (local geometry):** one nearest-neighbour signed link set `L = {±e₁, ±e₂, ±e₃} ≅ Fin 3 × Bool` with its prescribed octahedral rotation action `O`. Its rational function module has the projectors of `LinkDecomposition`; the *mathematical* complexification `V = ℂ^L` carries a chosen unitary/Hermitian interpretation. Neither `d=3` nor the simple-cubic *physical* graph is inferred from a gauge group ([SM] L63–75, L348–381; [LINK] L1–55, L465–488; [SUB] L143–163).
- **H (physical-carrier bridge):** if a physical interpretation is wanted, H-link is an equivariant identification of the observer/gauge carrier with `V`, **one copy `m=1`**. In general H-link allows `V ⊗ ℂ^m` and `K=6m`; it does not select `m=1`. A mere equal-dimensional vector-space isomorphism is insufficient for equivariant transport ([SM] L348–368; [LINK] L490–550).
- **C (kinetic and state data):** supply the complex structure, a positive-definite Hermitian inner product, the pre-condensate **custodially scalar** kinetic term with its assumed full `U(6)` action (H-cust), and an `O`-equivariant Hermitian state/condensate `Σ = aP₃ + bP₂ + cP₁` with **pairwise distinct real** `a,b,c`. The positive-frequency complex candidate away from null modes does not by itself source this physical structure; the H-cust condensate clause is an input ([SM] L332–344, L370–381; [#1211 c.6742071797](https://github.com/amaybaum/incompleteness/issues/1211#issuecomment-6742071797)).
- **Q (extra quotient, only if invoked):** separately choose the central subgroup `K_c = {(uI₃,vI₂,u²/v):u,v∈U(1)}` of `G₀=U(3)×U(2)×U(1)` and declare it redundant **for the action under consideration**. Amplitude-scale redundancy alone supplies at most the *common* circle and does not establish the second circle ([SM] L575–585; [GLOBAL] ``2–3; [NATIVE] ``1–2).
- **R (optional charged action):** separately supply the complex representations of `P=SU(3)×SU(2)×U(1)` on `Q=(3,2,1)`, `u_R=(3,1,4)`, `d_R=(3,1,-2)`, `L=(1,2,-3)`, `e_R=(1,1,-6)`, `H=(1,2,3)`, with last entries the **primitive integers `q=6Y`**; optionally require the matching determinant-character dressing of an action of `G₀`. Do not identify this with the raw `End(V)` conjugation action. The five chiral fields and Higgs are *selected fields*, not derived light excitations ([SM] L523–529, L575–599; [GLOBAL] ``4–5; [NATIVE] `3).
- **A (optional anomaly/normalization data):** for the five chiral representations `Q_L,u_R,d_R,L_L,e_R`, assume family-universal abelian charges, no additional charged chiral anomaly-cancelling fields, cancellation of the specified mixed and cubic anomalies, and **`Y_Q ≠ 0`** for the nonexceptional result. To display the conventional numerical charges, additionally adopt the charge normalization and electromagnetic identification. A Higgs/Yukawa version has its separate nonzero-Higgs-charge and coupling assumptions ([SM] L589–600; [HYPER] ``2–5).

**Then (mathematical conclusions):**

1. From **L**: invariant summands `V = V₃ ⊕ V₂ ⊕ V₁` of complex dimensions `3,2,1`, corresponding to `T₁,E,A₁`; the corresponding rational projector/dimension facts are already kernel-proved. The **pointwise commutant of the `O` action** on this multiplicity-one representation is `U(1)^3` in its unitary part; it must not be confused with the stabilizer below ([LINK] L263–326, L465–488; [SM] L370–381; [SUB] L163).
2. From **L + H + C**: `Stab_{U(6)}(Σ) ≅ U(3)×U(2)×U(1)=G₀`, of real dimension `9+4+1=14`. The full `U(6)` action is an *assumed custodial kinetic symmetry*, not derived by only decomposing the cubic representation ([SM] L340–344; [MATRIX] L25–31).
3. From **Q**, *as a separate optional group calculation*: `G₀/K_c ≅ S(U(3)×U(2))` with `Lie ≅ su(3)⊕su(2)⊕u(1)`. The quotient is constructive but the physical redundancy of `K_c` is not supplied by L/H/C or amplitude normalization ([SM] Proposition 14a, L579–585; [GLOBAL] `3).
4. From **R**, independently of **Q**: the specified charged-family-plus-Higgs action `ρ` of `P` has kernel `Z₆` generated by `(ωI₃,-I₂,e^{iπ/3})` (`ω³=1` primitive), hence faithful image `P/Z₆ ≅ S(U(3)×U(2))`. This is the **charged-action** kernel, not the raw endomorphism kernel. The isomorphism of the two *abstract target groups* alone does not identify the actual observed field action ([SM] Proposition 15a, L592–599; [GLOBAL] ``4–5).
5. From **A**, on the `Y_Q≠0` branch, the chosen chiral family satisfies `(Y_Q,Y_u,Y_d,Y_L,Y_e) ∝ (1,4,-2,-3,-6)`, with the `u/d` interchange, and conventional normalization yields `(1/6,2/3,-1/3,-1/2,-1)`. The independent `Y_Q=0` anomaly-free branch survives if this extra assumption is dropped ([SM] Theorem 15, L589–600; [HYPER] ``2–5).
6. From a *further chosen periodic cubic momentum/taste construction* (not needed for 1–5), the four corner pairs comprise one singlet pair and three axis-related pairs. The associated irreducible `T₁` triplet is on the **signed spin–taste vector carrier**, whereas the unsigned axis-pair label action is reducible (`A₁ ⊕ E`). The link tensor products/endomorphism space offer **representation availability** (e.g., cross-block tensor factors), not automatically the selected dressed hypercharge action, light particles, physical spin/chirality, or three realized generations ([TASTE] L95–155, L223–252; [SM] L432–466, L515–547).

No hypothesis above is `|S|<∞` or recurrence of all substratum states. This means the **implication** is independent of A1, **not** that OI has established an infinite-substratum model realizing every hypothesis.

## 2. Dependency ledger: proved versus imported data

The labels are intentionally narrow. *EXISTING CONDITIONAL ALGEBRA* means an established algebraic deduction **once its named inputs are supplied**, not an OI-native derivation of those inputs. A supplied fact without a native selector is *NON-NATIVE INPUT*. A missing mathematical/physical arrow is *PROOF GAP*. Where the source lacks enough to decide, use *INCONCLUSIVE*.

| Node / input or conclusion | Evidence and precise source | Provenance and status | A1 / locality audit |
| --- | --- | --- | --- |
| Site factorization and nearest-neighbour cubic spatial branch | [SM] L63–75; [SUB] L143–161 | **NON-NATIVE INPUT**; no native factorization or cubic-branch selector; #983 retains selection | Selecting a spatial branch is distinct from finite `S`; A4's actual periodic model class is finite |
| `d=3` in the full reconstruction | [SUB] L153–161; [SM] ``3.1–3.2, L202–210 | **NON-NATIVE INPUT** to this forward result. The manuscript's filters use E5–E7/continuum and observed physics, not a forward derivation from bare OI | No dimension-selection claim is imported into the algebra |
| Signed six-link set and `3⊕2⊕1` projectors | [LINK] L47–55, L120–326, L465–488; [SM] L370–381 | **EXISTING CONDITIONAL ALGEBRA** (geometry of *specified* cubic links; Lean projector/dimension/character results) | Finite **local** `Fin 3 × Bool` only; no finite number of sites or total configurations used |
| Equivariant transport of link decomposition | [LINK] L490–550, `hlink_transport` | **EXISTING CONDITIONAL ALGEBRA** under an *equivariant linear equivalence* | Does not construct the required physical equivalence or complex field |
| H-link with `m=1` and physical six-link carrier | [SM] L348–368; [MATRIX] L25–40 | **NON-NATIVE INPUT**; `m` not selected by degree-minimization | Finite local six-dimensional vector space is not finite `S` |
| Complex Hilbert/unitary lift and positive-frequency `J` | [SM] L340–344, L809; [#1211 accepted r5](https://github.com/amaybaum/incompleteness/issues/1211#issuecomment-6742071797) | **NON-NATIVE INPUT / PROOF GAP** for physical realization; positive-frequency candidate off null modes, not at null modes | A complex 6-dimensional model does not mean OI generates complex field operations |
| H-cust scalar kinetic term | [SM] Proposition 4b L332–338, Theorem 5 L340–344 | **EXISTING CONDITIONAL ALGEBRA** for *specified* symmetric-point complete-observer/counting model or H-blind extensions; **NON-NATIVE INPUT** for generic realized observer | Proposition's finite counting/symmetric observer case is **not** an A1-free derivation of physical H-cust; posit the scalar kinetic clause in this forward theorem |
| Equivariant `Σ` and distinct `a,b,c` | [SM] L340–344, L370–381 | **NON-NATIVE INPUT** (no native condensate construction or genericity selector) | Pointwise six-dimensional eigenspaces; no global count |
| `U(3)×U(2)×U(1)` stabilizer and `u(3)⊕u(2)⊕u(1)` | [SM] Theorem 5 L340–344; [MATRIX] L25–31 | **EXISTING CONDITIONAL ALGEBRA**, written stabilizer proof under H-link/H-cust/state input, not a Lean theorem here | Finite-dimensional local spectral algebra; independent of `|S|` |
| Cubic pointwise commutant versus block-algebra unitary group | [SUB] L163; [SM] L370–381 | **EXISTING CONDITIONAL ALGEBRA**; pointwise commutant unitary group `U(1)^3`, while *generic condensate* stabilizer is `U(3)×U(2)×U(1)` | Neither selects an observed gauge group |
| A6 endpoint covariance of coupled links | [SM] L114–120; [BACK] `a6cov_all` L147–164; [A6] `as1_leap_covariant` L535–551 | **EXISTING CONDITIONAL ALGEBRA** as a covariance **identity** transforming fields *and* link data; **PROOF GAP** for a native dynamical gauge connection | `BACK` works with finite reading sets on arbitrary site type; no all-site cardinality assumption in this identity |
| Removing central phases / choosing `K_c` | [SM] Proposition 14a L579–585; [GLOBAL] ``2–3 | **NON-NATIVE INPUT** for physical quotient. Common amplitude phase is insufficient; second independent circle must be supplied | Compact finite-dimensional groups; no recurrence |
| `G₀/K_c ≅ S(U(3)×U(2))` | [SM] Proposition 14a L579–585; [GLOBAL] `3 | **EXISTING CONDITIONAL ALGEBRA** (paper proof, kernel and surjectivity) | Local abstract group only; no finite total system |
| `P/Z₆` charged-family faithful image | [SM] Proposition 15a L592–599; [GLOBAL] ``4–5 | **EXISTING CONDITIONAL ALGEBRA** for the **specified action**; no native representation selector | No all-carrier finiteness |
| Raw full `End(V)` conjugation kernel | [SM] L583–585; [NATIVE] ``1–2 | **EXISTING CONDITIONAL ALGEBRA** with kernel `Δ=U(1)diag`, *not* `K_c` | Independent of `|S|`; blocks transfer is forbidden without proof |
| Nonabelian cross-block tensor representation availability | [SM] L475–529; [NATIVE] `3 | **EXISTING CONDITIONAL ALGEBRA** for spaces and determinant-character dressings; **PROOF GAP** for charged light chiral mode realization | `V⊗V*` is finite local module; source and choice of its physical action open |
| Periodic BZ corners and taste pairing | [TASTE] L95–155, L223–252; [SM] L302–304, L432–466 | **EXISTING CONDITIONAL ALGEBRA** for chosen periodic/corner label scheme; **NON-NATIVE INPUT** for its physical lattice and spin/taste interpretation | Needs appropriate periodic momentum/corner and parity structure; this is **not** used in stabilizer/quotient proofs. Checkerboard parity requires a period identification that preserves the two sublattices when that grading is invoked |
| H-spin', H-χ', physical matter selection | [SM] L445–466, L523–547, Theorem 13 L543–547 | **PROOF GAP**; the minimal SU(2) link-current embedding is taste-blind/vector-like in the cited control; specific selective mechanism not derived | Local algebra does not select physical three generations, spin, chirality, Higgs or spectrum |
| Fixed chiral family, `Y_Q≠0`, anomalies, normalization | [SM] L575–600; [HYPER] ``2–6 | **NON-NATIVE INPUT** for family/branch/anomaly requirements, **EXISTING CONDITIONAL ALGEBRA** for charge classification | Polynomial algebra only; no `|S|` |
| Full physical `SU(3)×SU(2)×U(1)` fields, bundle, line spectrum, Yang–Mills/QCD | [SM] L114–120, L593–599, L601–608; [SUB] L290–300 | **PROOF GAP / INCONCLUSIVE** for native realization and full global gauge choice; local charged action permits `Z₆` faithful image but not unique global line data | No implication from A1-free local Lie algebra to dynamics or observed particles |

**Important source-level qualification.** [SM] L428 and L511 contain strong *substratum-level* language about the gauge group/carrier, while [SM] L312, L340–344 and [SUB] L290–300 put the conditional unitary action on an **observer/emergent** structure. The accepted bridge audit records this level conflict ([#1211 c.6742071797](https://github.com/amaybaum/incompleteness/issues/1211#issuecomment-6742071797), F5; [#1211 c.6910248680](https://github.com/amaybaum/incompleteness/issues/1211#issuecomment-6910248680), GAUGE-N3). This audit takes the narrower, actually premised observer-level reading; it **does not correct the manuscript** or assert an unsupported map identifying the two levels.

## 3. Algebraic checkpoints and action separation

### 3.1 Stabilizer, commutant and Lie algebra are different claims

For the specified signed-link module, [LINK] proves projectors with ranks `3,2,1` and an internal direct sum, commuting with the signed-axis symmetries. Schur's lemma then applies to the prescribed inequivalent irreducible blocks. The **pointwise unitary commutant of the cubic action** is `U(1)^3`. The **unitary group of the block algebra** is `U(3)×U(2)×U(1)`. With full custodial `U(6)` symmetry and distinct condensate eigenvalues, the latter is also the **unitary stabilizer of `Σ`**. These descriptions must not be collapsed into a claim that merely commuting with `O` furnishes all unitary block rotations. Source: [SM] L340–344, L370–381; [SUB] L163; [LINK] L465–488.

Thus `Lie(Stab(Σ))=u(3)⊕u(2)⊕u(1) = su(3)⊕su(2)⊕u(1)^3`. The familiar `su(3)⊕su(2)⊕u(1)` is available **after** a separate two-dimensional central identification or the stated faithful charged action, not after simply disregarding a common phase. Source: [SM] L575–585; [GLOBAL] ``2–3.

### 3.2 Two distinct quotient/action constructions

**Abstract correlated quotient:** [SM] Proposition 14a/[GLOBAL] `3 define a surjective `F:G₀→S(U(3)×U(2))` with
`F(C,D,t)=(t⁻² det(C)det(D)⁻¹ C,\ t³ det(C)⁻²det(D) D)`
and `ker F=K_c={(uI₃,vI₂,u²/v)}`. The first-isomorphism argument is existing exact paper mathematics. One circle is the common scalar phase; the other is *not* established as redundant by amplitude-scale gauge. The abstract quotient does not prescribe what happens to each raw microscopic mode.

**Selected charged-family action:** [SM] Proposition 15a/[GLOBAL] ``4–5 supply `P=SU(3)×SU(2)×U(1)` with integer weights `(1,4,-2,-3,-6;3)` for `(Q,u_R,d_R,L,e_R;H)`. The `d_R`, `L` and `e_R` components force any common kernel element to satisfy `A=z²I₃`, `B=z³I₂` and `z⁶=1`; the other listed components then act trivially. Hence the kernel is exactly the cyclic `Z₆` in `P`. This is a *specified representation*, not the unique representation of the geometric link carrier. The global target `S(U(3)×U(2))` is isomorphic to `P/Z₆`, but other compatible global line/bundle choices remain unselected ([SM] L592–599).

**Raw endomorphism action:** on `End(V₃⊕V₂⊕V₁)`, `G₀` acts by `X↦gXg⁻¹` with `g=diag(C,D,t)`. Its kernel is precisely `Δ={(uI₃,uI₂,u)}`; the faithful image is `G₀/Δ`, with **two** central Lie directions (`su(3)⊕su(2)⊕u(1)^2`), not the one of `G₀/K_c`. The additional `K_c/Δ` circle acts on cross-block Homs, and there is no established native map that kills it. Restricting only to block-diagonal End spaces changes the kernel again. Source: [NATIVE] ``1–3; [SM] L583–585. **Never transfer `ker ρ=Z₆` or `ker F=K_c` to this raw action.**

### 3.3 Hypercharges are conditionally classified, not produced from link dimensions

[HYPER] ``2–3 give, with `a=Y_Q` and `(a,u,d,\ell,e)` the selected right-handed-particle conventions, the relevant anomaly equations
`C=2a-u-d=0`, `W=3a+\ell=0`, `G=6a-3u-3d+2\ell-e=0` and `A=6a³-3u³-3d³+2\ell³-e³=0`.
The **existing** algebra implies `d=2a-u`, `\ell=-3a`, `e=-6a` and `A=-18a(u-4a)(u+2a)`. Thus:

- If `a≠0`, `(a,u,d,\ell,e)=(a,4a,-2a,-3a,-6a)`, up to swapping `u,d`.
- If `a=0`, the distinct anomaly-free family `(0,b,-b,0,0)` remains.

The conventional values need `a=1/6` and the electric-charge/field-label interpretation; if additional charged right-handed neutrinos or family nonuniversality are allowed, the uniqueness premises change ([HYPER] ``4–6). This is not a native selection of the chiral family, the allowed matter spectrum, or the physical charge normalization.

### 3.4 Background independence gives covariance, not native selection or Yang–Mills dynamics

At endpoints `i,j`, a supplied link variable may transform `M_{ij}↦g_i M_{ij}g_j^{-1}` while fields transform `ϕ_i↦g_iϕ_i`. The link-coupled update is then covariant, including the second-order leap when the additive structure is present; the Lean lemmas explicitly prove this interface identity for arbitrary neighbourhoods/couplings ([BACK] L147–164; [A6] L535–551). It does **not** constrain the transformed link rule to select one gauge algebra, produce `M` from `ϕ`, give a gauge-invariant physical measure, establish the Wilson action as dynamics, or prove QCD ([SM] L114–120, L801–813). These are downstream source obligations, not conclusions of the local group theorem.

## 4. Mandatory negative controls

| Control | Source-proven counterfactual | What fails | Required conclusion |
| --- | --- | --- | --- |
| **NC-Σ: coincident condensate values** | If `a=b≠c` in `Σ=aP₃+bP₂+cP₁`, the full `U(6)` stabilizer is `U(5)×U(1)`, **not** `U(3)×U(2)×U(1)`; if all three equal it is `U(6)`. Follows directly from the spectral stabilizer statement in [SM] Theorem 5 L340–344 | Dropping the pairwise-distinct hypothesis invalidates the advertised *generic* stabilizer | **NON-NATIVE INPUT:** genericity is load-bearing; no physical mechanism selecting its block spectrum was proved |
| **NC-End: different raw kernel** | For all `X∈End(V)`, trivial conjugation by `g∈G₀` implies `g` is common scalar (`ker=Δ`). The extra `(I₃,uI₂,u⁻¹)∈K_c` has nontrivial action on cross-block Hom spaces for `u≠1` ([NATIVE] ``1–2; [SM] L583–585) | The native raw `End(V)` action does **not** factor through `G₀/K_c` and is not the selected charged-family action | **PROOF GAP:** an observer field/action, mode projection or justified redundancy must be sourced before promoting `Z₆` to a physical native kernel |

Two **additional existing scope controls**, not new experiments: [HYPER] `6 exhibits `Y_Q=0` and enlarged-family anomaly counterbranches, and [TASTE] L223–252 distinguishes the signed irreducible triplet from the reducible unsigned label action. Neither is repaired by the link decomposition.

## 5. Finiteness audit — three non-equivalent properties

| Property | Where actually used | A1-free verdict |
| --- | --- | --- |
| **Local finite-dimensional algebra**: six link directions, rational rank-6 module and chosen complex Hermitian dimension-6 lift | [LINK] L47–55, L263–326, L465–550; [SM] L340–381 | **EXISTING CONDITIONAL ALGEBRA**; this is finiteness of a **single local module**, not `|S|<∞` |
| **Finite/local reading sets on arbitrary site index types** | [BACK] `a6cov_all` L147–164, [A6] `as1_leap_covariant` L535–551 | **EXISTING CONDITIONAL ALGEBRA** for A6 covariance interfaces; finite neighbours do not require a finite set of all sites |
| **Lattice periodicity, Fourier corners and checkerboard compatibility** | [SUB] L153–161 (A4 class); [SM] L286–298, L432–466; [TASTE] L95–155 | **NON-NATIVE INPUT** for the taste/dimensional branch; periodic momentum/corner and parity-compatible identification are separate structural conditions, not needed for the pointwise stabilizer |
| **Finite total substratum `S`, exact recurrence, finite hidden counting** | [SUB] Theorem 23 L193–195 and Stage 1 L119–139; [SM] L44, L63–70, Proposition 4b L332–338 | **NOT USED** in the abstract algebra's arguments 1–5 above; cannot use finite counting in Proposition 4b as proof of an A1-free *physical* kinetic mechanism |
| **Native infinite-carrier existence with observer/H-link/state/charged action** | No construction in the audited sources; [MATRIX] L21–40 and [SUB] L290–300 delimit it | **PROOF GAP / INCONCLUSIVE**: neither a finite total carrier nor an infinite carrier is realized by the local algebra alone |

**Precise conclusion on A1:** The forward implications of `1 need no global cardinality/recurrence step. However the currently chosen **finite periodic site/lattice plus finite local alphabet** model class may already entail a finite total configuration space (the [MATRIX] source pin explicitly notes this). Therefore simply dropping the textual word “finite” from the complete Theorem 23 or its A4 model is **not** a construction of a genuinely infinite substratum. An abstract pointwise representation on any carrier with supplied six links is mathematically well-formed; realizing it with OI's native dynamics and embedded observer is a different, open proof.

## 6. Physical-source obligations and scope fences

These are **not** consequences of this result and are not newly authorized programmes:

1. **Observer/complex-carrier bridge — PROOF GAP:** derive, on a specified actual OI dynamics/observation interface, the observer-level complex six-link field, its Hermitian metric and chosen complex structure (including null-mode handling), with an equivariant H-link map and *single-copy* `m=1`, rather than imposing these ([SM] L63–75, L340–368; [SUB] L290–300; #1211). The full quantum-source bridge itself remains #1211's scope.
2. **Kinetic and condensate mechanism — NON-NATIVE INPUT / PROOF GAP:** source H-cust and a dynamically realized `O`-equivariant Hermitian condensate with **three distinct** eigenvalues, and establish its actual physical coupling to the selected carrier ([SM] L332–344; [MATRIX] L25–40). The A1-08 observer-field investigation is separate and not performed here.
3. **Native central redundancy and physical charged action — PROOF GAP:** show which observer modes survive, why a second central circle is redundant or why the *specified determinant-dressed* charged family/Higgs action is native; reconcile it with the raw `End(V)` kernel, including global bundle and line-operator data ([GLOBAL], [NATIVE], [SM] L579–599).
4. **Matter/selection — PROOF GAP:** select the five chiral representations, Higgs and actual light propagating spectrum from the **available** tensor factors, with H-spin', H-χ' and tastes/physical-generation identification, correct statistics and removal/gapping of mirror or exotic modes ([SM] L475–547). Anomaly cancellation cannot select this set in advance.
5. **Gauge dynamics / QCD — PROOF GAP:** identify native link variables and their probability law, a Yang–Mills-type action/dynamical propagator, couplings and running, the QCD non-Abelian sector and its observed consequences. Covariance/plaquette invariance alone is insufficient ([SM] L114–120, L601–608, L801–813). Full global form also depends on allowed line/bundle data.
6. **One common physical OI realization — INCONCLUSIVE:** prove that a chosen OI substratum and observer interface jointly realize the selected cubic branch, conditional gauge algebra, charged/matter operations and experimental/quantum prerequisites. This cannot be inferred from the reverse E1–E7 reconstruction in [SUB] `3, or by borrowing #1211's missing wave/operator/Bell mechanism ([SUB] L193–205; [#1211 accepted r5](https://github.com/amaybaum/incompleteness/issues/1211#issuecomment-6742071797)).
7. **Lattice/gauge uniqueness — separate #983:** no inference from observed SU(3)×SU(2)×U(1), from Bravais comparisons, or from anomaly consistency back to OI-native selection of simple-cubic geometry; [SM] L386–416 is a restricted *reverse/empirical compatibility* argument. This unit asserts no uniqueness of physical model.

**Stop-rule outcome:** A1-C04 reaches **EXISTING CONDITIONAL ALGEBRA** for the specified local representation/stabilizer and for the *separately chosen* group/charged action/charge classifications. It reaches **PROOF GAP** at the first requested native physical-carrier and kinetic/condensate/charged-action sources. This is **not** a derivation of the physical Standard Model, realized gauge bosons, physical generations or masses, Yang–Mills/QCD, operational quantum mechanics or a complete A1-independent substratum. A1 remains open and unadopted. **Physical source: NOT PASSED.**

## 7. Source index, verification method and review request

All GitHub file links below refer to commit `6eac91ee25a1afaea4ed148b0c54967a08b12ac3`, not mutable `main`. `file:lines` locators in the text refer to line numbers of these sources.

- [MATRIX]: `verification/audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md`, especially L5–15 and **P12(a), L21–40**. Existing recovery verdict A, expressly conditional.
- [SUB]: `papers/Substratum.md`, especially Stage 2 L143–169, Theorem 23 L189–205, hierarchy L290–300.
- [SM]: `papers/SM.md`, especially `2.4 L63–75, A6 L114–120, Proposition 4b / Theorem 5 L332–344, H-link / Theorems 6–7 L348–385, restricted Bravais selection L386–416, taste/matter L432–547, Theorems 14/15 and Propositions 14a/15a L575–600, gauge dynamics caveats L801–813.
- [LINK]: `verification/lean-mathlib/OIBridge/LinkDecomposition.lean`, especially L1–55, L263–326, `theorem_7` L465–488 and `hlink_transport` L490–550.
- [TASTE]: `verification/lean-mathlib/OIBridge/TasteBranching.lean`, especially `theorem_8` L223–252.
- [BACK]: `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, especially `a6cov_all` L147–164.
- [A6]: `verification/lean-mathlib/OIBridge/A6Instantiation.lean`, especially `as1_leap_covariant` L535–551.
- [GLOBAL]: `verification/audits/manuscript/theorem-recovery-20261028/gauge-global-form/global_form_proof_v1.txt`, ``2–5: correlated quotient, `Z₆` faithful image and proof.
- [NATIVE]: `verification/audits/manuscript/theorem-recovery-20261028/gauge-global-form/native_carrier_barrier_v1.txt`, ``1–3: raw conjugation kernel and nontrivial second center.
- [HYPER]: `verification/audits/manuscript/theorem-recovery-20261028/gauge-global-form/hypercharge_recovery_v1.txt`, ``2–6: conditional anomaly classification and controls.

**Method:** read-only source and declared theorem inspection; transcribed the existing algebraic proof dependencies, with the two source-proven negative controls. No new computation, Lean run, simulation, physical assumption, proof adoption or manuscript edit. Claiming the Lean checks remain green at this head requires independent CI evidence and is **not** asserted here.

**Requested independent review of exact author head:** (i) verify every input/output/source locator against pinned files and whether any stabilizer/charged-action claim illicitly uses the raw `End(V)` kernel; (ii) check whether the paper-level `U(6)`/complex and H-cust hypotheses are sufficient as *explicit supplied* assumptions; (iii) check that neither periodicity nor total finiteness was silently used in the restricted group proof; (iv) check the exceptional hypercharge branch and additional-family caveats; (v) issue ACCEPT / REVISE with exact SHA. Review acceptance would not authorize manuscript promotion or merge.

[MATRIX]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md
[SUB]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/papers/Substratum.md
[SM]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/papers/SM.md
[LINK]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/lean-mathlib/OIBridge/LinkDecomposition.lean
[TASTE]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/lean-mathlib/OIBridge/TasteBranching.lean
[BACK]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/lean-mathlib/OIBridge/BackgroundIndependence.lean
[A6]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/lean-mathlib/OIBridge/A6Instantiation.lean
[GLOBAL]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/audits/manuscript/theorem-recovery-20261028/gauge-global-form/global_form_proof_v1.txt
[NATIVE]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/audits/manuscript/theorem-recovery-20261028/gauge-global-form/native_carrier_barrier_v1.txt
[HYPER]: https://github.com/amaybaum/incompleteness/blob/6eac91ee25a1afaea4ed148b0c54967a08b12ac3/verification/audits/manuscript/theorem-recovery-20261028/gauge-global-form/hypercharge_recovery_v1.txt
