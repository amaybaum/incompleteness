# Locality round LOC-1 — how locality verdicts depend on the identification of parts: PREREGISTRATION (draft)

**Status: drafting, native V3; not a candidate `F`.** Drafted on a pull request from `D` for owner review. The owner's
decisions of 2026-10-16 are applied (*Owner decisions*). Three design decisions, (a), (e) and (f), are still the
owner's; until they are made, this text carries the proposed option, marked *proposed*. Nothing is executed. No
workflow is dispatched for this round, and its code is not run on any target object before `F`. Only the owner
designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round LOC-1
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/
record AM verification/receipts/LOC-1.json
```

D: fc5abade2a8ca381caedaa93c0441570fc060319. It is `main` after #851, #849 and #850, and its push run 38870075770
concluded `success`.
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory. **No manuscript, built
artifact, module, census entry, probe, workflow, coverage-ledger entry or research record outside the record directory
changes under any outcome.** The P0 and P2 research records are cited as provenance and are not edited.

## 1. The question

Every locality verdict on record is computed in a **declared** identification of the parts. P0 declares
`V ≅ V₁ × V₂` and `A ≅ A₁ × A₂`. P2 declares regions and takes each site's current component as the visible datum.
Site factorization is posit-ledger item (viii) (Main §4.5, from #851): given an identification, the dynamics
determines its coupling graph, and the dynamics alone has not been shown to select it. SM §2.4 states that selection
question as open. This round asks, for frozen configurations only, three questions in three nested scopes:

- **I0.** Which product identifications are compatible with the visible observational law, and do P0's recorded
  exclusions hold under all of them?
- **I1.** Which of those also preserve the independently specified observer registers and readout?
- **I2.** Which of those also satisfy an explicitly specified dynamical compatibility condition, and is the
  identification then unique?

`I2 ⊆ I1 ⊆ I0` in every case. The spatial identification is never assumed in a cell that could recover it: it enters
as one special identification among those enumerated, searched or sampled, and as the declared reference `σ₀`.

## 2. Records the round uses

Each is used only as stated.

| item | where | status |
| --- | --- | --- |
| P0's definitions: carriers `𝒪₁`–`𝒪₃`, `SL-U`, PC, RL, the frozen lifts and conventions | P0 `RULES.md`, blob `988b4fe2`; `p0_exact.py`, blob `85251bb2` (sha256 `00cb032b…`); at `55450d57`, `plan/p0-evolution-source-20261013` (#834) | research record, frozen |
| P0's recorded statuses and pair verdicts | P0 `p0-exact-output.txt`, blob `b34eb953`, lines 15–76 and 113–178 | research record |
| P2's configurations and register convention | P2 `RULES.md`, blob `d0b286ea`, §3–§4; `p0_ls_exact.py`, blob `41905335` (sha256 `904e242e…`); at `ea9a6b71`, `research/p2-locality-sources-20261015` | research record |
| the cone consumes site factorization and a neighbourhood function only | `iterate_dependsOnlyOn_ball`, RegionTower.lean:283 (at `D`) | kernel theorem |
| visible configurations are registered values of a finite set | Main.md:48 (Lemma 1) | lemma |
| deep sectors decoupled from the boundary are gauge | Substratum.md:92, Theorem 24(iii) | cross-check only (§7.S) |

*Proposed (f):* the frozen configurations, lifts and conventions are **ported** into the record directory at stage 1
(`objects/`), each pinned to its research commit by blob and checked by K-repro, so that the round runs from its own
record without depending on unlanded branches. Not adopted, and used only as objects of test: any identification
principle, `SL-U`, coupling-degree minimization and regional independence.

## 3. Definitions

### 3.1 Identifications and their classes

- **Set level (leg T).** An identification of a finite set `X` with `Fin m × Fin n` is a bijection `σ`. Relabelling
  each factor's alphabet is post-composition with `S_m × S_n`.
- **Pairs.** An identification of `V × A` is a pair `σ = (σ_V, σ_A)` at P0's declared factor shapes.
  - Two pairs are equivalent when they differ by alphabet relabellings of the four factors, or by the swap of the two
    parts `V₁ × A₁ ↔ V₂ × A₂`, applied to `σ_V` and `σ_A` together.
  - Swapping the factors of `V` alone is not quotiented: it would pair `V₁` with `A₂`, which is a different cut, not a
    relabelling.
  - No carrier, product test or condition below distinguishes within a class (W-REL).
  - `D(C)` is the set of classes. One representative is used per class, and on `A` it sends the anchor to `(0,0)`
    (W-CLS).
  - The declared identification is `σ₀ = (id, id)`.
- **Transport.** `U^σ = P_σ U P_σᵀ`, with `P_σ` the permutation matrix of `(i, a) ↦ (σ_V(i), σ_A(a))` in P0's index
  convention; `L^σ = (U₀^σ, U₁^σ)`; `Γ^σ = P_{σ_V} Γ P_{σ_V}ᵀ`.
- **Linear (leg S).** A linear decomposition of `F_q^n` is an unordered set of `n` linearly independent functionals,
  each up to a nonzero scalar, represented by an invertible `B` whose rows are the functionals. The scalars relabel a
  factor's alphabet and the order relabels sites. The count is `|GL(n,q)| / ((q−1)ⁿ n!)` (W-CLS-S). Nonlinear
  identifications are out of scope.
- **Not quotiented.** The centralizer `C(M) = {X ∈ GL(n,q) : XM = MX}` of a rule, the φ-pullback among its elements,
  and any other symmetry of the dynamics. Quotienting by them would hide the non-uniqueness under test. Minimizers are
  reported with their centralizer orbits instead.

### 3.2 The scopes

**Leg T** (P0's configurations `C`, frozen lifts `b`):

- **I0(C)** *(proposed reading (a))* is the set of `σ ∈ D(C)` with `Γ^σ` a product, by PC on P0's `cut_stoch`: the
  visible law is the law of two uncoupled parts in `σ`, which is what `SL-U` needs in order to apply at all.
- **I1(C)** is the set of `σ ∈ I0(C)` with `σ_V` in the declared register class. The registers are the visible
  configurations with their declared readout into `V₁` and `V₂`; `σ_A` is free.
- **I2(C, b)** is the set of `σ ∈ I1(C)` under which `b` is **regionally independent**: both `U_t^σ` reshuffle across
  the cut to rank 1. The condition is on the dynamics `b` itself, and it discriminates: it fails for most
  identifications of a coupled lift, and it is not satisfied by an identification merely because it conjugates the
  dynamics (SC-I2). Regional independence of `b` is `SL-U`'s admission criterion for `b` (P0 RULES:86–88, :274–275), so for a
  recorded exclusion its content is fixed in advance by W-I2T, and the cell's measured content is its size for every
  frozen lift. It is an **assumption** wherever a reading uses it, and the reading says so.

**Leg S** (P2's linear rules `M`, registers by P2's convention):

- **I0(M)** is the set of all linear decompositions of the rule's space.
- **I1(M)** is the set of decompositions in which every register functional is one of the decomposition's functionals,
  up to scalar.
- **I2(M)** is the set of decompositions in I1 with a bipartition `W₁ ⊔ W₂` of the functionals that puts each region's
  registers in `span W_k` and makes each `span W_k` invariant under `f ↦ fM`, so that no coupling edge crosses the
  regional cut. The condition refers to no site coordinate: it is a condition on subspaces generated by the registers
  and the dynamics. It is an **assumption** (regional independence), and every token read in I2 says so.
- **The closure** `Z_k = span{ f Mʲ : f a register of region k, j ≥ 0 }` decides I2 without enumeration (W-OBS).

### 3.3 Verdicts of a frozen lift `b` on carrier `𝒪ₓ` under `σ` (leg T)

At P0's frozen times; the first case that applies is the verdict.

1. **ADMITTED(σ):** both `U_t^σ` reshuffle to rank 1, by PC on `cut_operator`.
2. **SEP-PHYS(σ):** some value of `𝒪ₓ(L^σ)` is a non-product, by PC.
3. **SEP-REP(σ),** for `x = 1` only: at each `t` the reshuffled Choi matrix of `𝒪₁(L^σ)(t)` has rank 1 with factors
   `C¹_t`, `C²_t`, and `rank C^k_t ≤ |A_k|`. By W-REP some admitted lift attains the value.
4. **PROD(σ),** for `x ∈ {2, 3}`: every value is a product; attainability is not certified.
5. **OPEN(σ)** otherwise.

At an EXCLUDES-ALL configuration (`CCC`, `CENT`), a `σ` with `Γ^σ` a non-product has verdict EXCLUDES-ALL(σ).

### 3.4 Invariance classes of a recorded exclusion `e = (C, b, x)` over a scope `S`

**A proven invariance and an observed one are different tokens.**

| class | definition |
| --- | --- |
| **INV** | SEP-PHYS(σ) for **every** `σ ∈ S`, established by exhaustive enumeration of `S`, by the complete search S16 terminating (W-SEP), or by a written statement checked by its control. For an EXCLUDES-ALL `e`, it means `S = ∅` |
| **INV-SAMPLED(N)** | SEP-PHYS(σ) for each of the `N` identifications examined (stratified samples and targeted identifications, §5), where `S` was not covered. **This is an observation, not an invariance**, and no reading states it as one |
| **REL** | some `σ ∈ S` gives ADMITTED(σ), or SEP-REP(σ) when `x = 1`; for an EXCLUDES-ALL `e`, some `σ ∈ S` gives the frozen lift ADMITTED, or SEP-REP on `𝒪₁`. One witness establishes it, sampled or not |
| **REL-PROD** | `x ∈ {2, 3}`, not REL, and PROD(σ) for some `σ ∈ S` |
| **OPEN** | anything else |

Leg S uses the same split: a statement about every decomposition of a space is proved only where the space is
enumerated or decided by closure; on a sampled space it carries `-SAMPLED(N)`.

## 4. Frozen configurations

### 4.T Leg T (P0's, verbatim)

| config | lifts | recorded exclusions (P0 output, blob `b34eb953`) | `D(C)` classes |
| --- | --- | --- | --- |
| `CCT4` | all nine | `Lcc` `𝒪₁`; `We.X` `𝒪₁` `𝒪₂` `𝒪₃`; `WW.Ke` `𝒪₂` `𝒪₃` | 18 |
| `CCC` | `Ucv` | EXCLUDES-ALL | 18 |
| `CENT` (countercontrol) | `CN` | EXCLUDES-ALL | 3 |
| `C21` | all twelve | `F` `𝒪₁`; `T` `𝒪₁`; `PF` `𝒪₁` `𝒪₂` `𝒪₃`; `Wd.P` `𝒪₁`; `Wd.PQ` `𝒪₁` `𝒪₃`; `PQ.Dn` `𝒪₁` `𝒪₂` `𝒪₃` | `16!/(4!²·2)` = 18,162,144,000 × 1 |
| `C1A`, `C1B`, `CELIM` (controls) | P0's | none | 1 × 1 |

### 4.S Leg S

| id | rule | space | scopes |
| --- | --- | --- | --- |
| `S-edge1(α)` | one 2-site edge, `F c 0 = α c₁`, `F c 1 = α c₀`, `q = 3`, `α ∈ {1, 2}` | `F_3^4` | I0 exhaustive (63,180; owner exception), I1, I2 |
| `S-free` | P2's `U-free(3)`; regions `{0} \| {1}`; registers at both sites | `F_3^4` | I0, I1, I2 exhaustive |
| `S-deep` | two isolated sites, `q = 3`; regions `{0} \| {1}`; a register at site 0 only | `F_3^4` | I2 exhaustive (the unobservable case) |
| `S-ring(q)` | ring of 4 sites, `(p, c) ↦ (c, A c − p)`, `A` the ring adjacency, `q ∈ {3, 5}` | `F_q^8` | I0 by special decompositions and 2,000 stratified samples; I1 and I2 by closure |
| `S-edge2(α,β)` | P2's `U-edge(3, α, β)`, `α, β ∈ {1, 2}`; regions are the edges; registers at all sites | `F_3^8` | I2 by closure |
| `S-edge2-sparse` | `U-edge(3,1,1)` with registers at sites 0 and 3 only | `F_3^8` | I2 by closure |
| `S-cut` | P2's `C-cut`; regions `{0,1} \| {2,3}` | `F_3^8` | coupled countercontrol, by closure |
| `S-chain` | P2's `C-chain`; regions `{0} \| {5}` | `F_3^{12}` | coupled countercontrol, by closure |

## 5. Special identifications, wherever defined

Each is evaluated in every scope it belongs to and reported by name beside the enumerated, searched or sampled results.

- **Spatial:** `σ₀` (leg T) and the natural decomposition (leg S).
- **Eigenmode:** the ring adjacency's eigenbasis where it diagonalizes over `F_q` (`q = 3`: columns `(1,1,1,1)`,
  `(1,−1,1,−1)`, `(1,0,−1,0)`, `(0,1,0,−1)`; `q = 5`: Fourier with `ω = 2`).
- **Dynamics-transported:** the φ-pullback `β ∘ φ` of each special decomposition (leg S); for leg T, the
  identification transported by `τ` for `T` (W-T) and the parity relabelling `(i₁,i₂) ↦ (i₁, i₁ ⊕ i₂)` (W-PAR),
  applied to `V` and to each factor of `C21`'s grid.

## 6. Written statements [W]

Proofs go in the result note. Each is checked where §8 says.

- **W-REL.** Post-composition with `S_m × S_n` (and the swap when `m = n`) preserves every product test, every carrier
  value up to the same relabelling, and regional independence. Scalars and order do the same for linear
  decompositions. So each quotient is by relabellings only.
- **W-CLS.** A 4-point set has 6 identifications with `Fin 2 × Fin 2` up to `S_2 × S_2`, and 3 up to the factor swap as
  well.
  - At `CCT4` and `CCC`, `D(C)` therefore has 6 · 6 / 2 = 18 classes. Fixing the class of `σ_V` up to `S_2 × S_2` leaves
    6, the I1 ambient.
  - At `CENT`, where `A` is trivial, the counts are 3 and 1.
  - The alphabet group acts transitively on grid points, so every class has a representative sending a given point to
    `(0,0)`.
  - An `m`-point set has one class with `Fin m × Fin 1`.
- **W-CLS-S.** `F_3^4` has `|GL(4,3)| / (2⁴ · 4!) = 63,180` linear decompositions: the unordered independent 4-subsets
  of the 40 points of `PG(3,3)`.
- **W-HID.** If `σ_A` fixes the anchor, every carrier value of `L^{(σ_V, σ_A)}` equals that of `L^{(σ_V, id)}`:
  `𝒪₁`–`𝒪₃` read only anchored columns and sum over the hidden label. So SEP-PHYS(σ) and PROD(σ) depend on `σ_V` alone.
- **W-I2T.** Let `e = (C, b, x)` be a recorded SEP-PHYS exclusion certified by PC (every recorded exclusion of §4.T
  is; P0's single-point certificate occurs only at the `CELIM` control, P0 output line 177). Every `σ ∈ I1(C)` has `σ_V` in the declared class, so
  by W-HID and W-REL some value of `b` is a non-product under `σ`; by RL an admitted lift has only product values. Hence
  `b` is ADMITTED under no `σ ∈ I1(C)`, and `I2(C, b) = ∅`. For an EXCLUDES-ALL `e`, `Γ^{σ₀}` is a non-product and `Γ^σ`
  depends on `σ_V` alone, so `I1(C) = ∅`. **So for every recorded exclusion, I2 is empty by this statement; the cell
  checks it by enumeration, and its informative content is `|I2(C, b)|` for the admitted lifts.**
- **W-REP.** If `𝒪₁(t) = E¹_t ⊗ E²_t` at `t = 0, 1`, with `E^k_t` CPTP of Kraus rank at most `|A_k|`, a Stinespring
  isometry anchored at `a₀ₖ` exists on `V_k × A_k`; extended to unitaries `U^k_t`, the lift `(U¹₀ ⊠ U²₀, U¹₁ ⊠ U²₁)` is
  admitted and attains the value; coherence follows as in P0's RL.
- **W-CYC.** A deterministic law given by a permutation `π` is a product under `σ` iff `σπσ⁻¹ = π₁ × π₂`. On `2 × 2`
  the product permutations have cycle type `1⁴` or `2²`, so CNOT is a product under no identification. **W-CYC-16:** a
  transposition on 16 points is never `π₁ × π₂` on `4 × 4`, since `|Fix π₁| · |Fix π₂| = 14` has no solution with
  factors at most 4.
- **W-T.** `T = P_τ (H₁ ⊠ Hᵢ) P_τᵀ`, with `P_τ` a permutation of `V` and `|A| = 1`. Under the identification transported
  by `τ`, `T^σ = H₁ ⊠ Hᵢ`, which is admitted. `Γ ≡ 1/16` is a product under every identification.
- **W-PAR.** The relabelling `(i₁, i₂) ↦ (i₁, i₁ ⊕ i₂)` of `Fin 2 × Fin 2` maps `X ⊗ X` to `X ⊗ 1`.
- **W-EQ1u.** A unitary channel on `V₁ ⊗ V₂` is a product channel iff the unitary is a product up to phase.
- **W-COL.** If `M^σ = M¹ ⊗ M²`, then for each fixed column index `y` the map `x ↦ M[x][y]` read on the grid through `σ`
  has rank 1, and likewise for rows. These are necessary conditions on `σ` alone.
- **W-SEP** (completeness of S16). Every class has a representative with `σ(0) = (0,0)` (W-CLS); every pruning test is
  necessary (W-COL); so a search that terminates returns every class passing the final PC test.
- **W-PB.** For `X ∈ C(M)`, `G_{BX} = G_B`; with `B = M` (the φ-pullback), `G_M = M`. The φ-pullback is the same
  factorization as the natural one iff `M` is monomial.
- **W-OBS.** A regional uncoupled decomposition has `span W_k ⊇ Z_k`, so one exists only if `Z₁ ∩ Z₂ = 0`. If
  `Z₁ ⊕ Z₂` is the whole dual space, the assignment is unique and equals `(Z₁, Z₂)`. If it is a proper subspace, the
  unobservable complement can be assigned in more than one way and influences no register.

## 7. Cells and decision rules

All arithmetic is exact: `Fraction`; P0's `ℚ(ζ₁₆)` class, ported, for `C21`; integers mod `q` for leg S. Every token
prints from measurements. The decision rules fix what each measurement decides; they fix no expected number.

### 7.T Leg T

- **T-I0, at `CCT4`, `CCC`, `CENT`:** for every recorded exclusion and every `σ ∈ D(C)`, compute `Γ^σ`'s product status
  and the verdict of §3.3, then the class of §3.4 over I0(C). Exhaustive.
- **T-I0, at `C21`:** by the search S16 (below), per lift and recorded carrier. Targets: for `𝒪₁`, `U₀` and `U₁`
  together; for `𝒪₃`, `U₁U₀ᴴ` and `U₀U₁ᴴ` (W-EQ1u); for `𝒪₂`, `R(1,0)` and `R(0,1)`.
  - **S16:** fix `σ(0) = (0,0)`; assign `σ(1), σ(2), …` in index order to unused grid points, breaking the remaining
    class symmetry as measured at drafting (§9); after each assignment apply W-COL's tests to every target on the
    assigned points; at a complete assignment apply PC to every target; deduplicate by the class group.
  - **Budget (owner decision (b)):** no unrestricted enumeration. A node budget per (lift, carrier), fixed in §9 from
    the measured costs. **Termination** gives an exact class: INV, REL or REL-PROD. **Exhaustion** gives the fallback:
    the special identifications of §5, then 2,000 reproducible identifications stratified as §9 fixes, then the class
    of §3.4 with INV replaced by INV-SAMPLED(N). The node count is reported either way.
- **T-I1:** the class of each recorded exclusion over I1(C). By W-HID it equals the class at `σ₀`; the cell checks that
  exactly (K-hid) and reports it as a consequence of fixing the visible registers, not as a finding.
- **T-I2:** for every frozen lift `b`, enumerate I2(C, b) over I1(C) (at most 6 classes at `CCT4` and `CCC`; 1 at `CENT`
  and `C21`). For each recorded exclusion, check `I2(C, b) = ∅` against W-I2T. For each admitted lift, report
  `|I2(C, b)|` and print **`T-I2-UNIQUE`** (one class), **`T-I2-NONUNIQUE`** (two or more) or **`T-I2-NONE`**. Where
  `|I1(C)| = 1` (`CENT`, `C21`) a single class is fixed by I1 already, and the token is printed as **`T-I2-UNIQUE(I1)`**,
  which no reading counts as uniqueness given regional independence. Any leg-T I2 case not computed, for any reason,
  prints **`T-I2-UNRESOLVED`** with the reason; it is never omitted silently and never read as empty.
- **T-F5** (P0's NS-WEAKER witnesses `Lcc`, `WW.Ke`, `Ucv`), over I0: **`LOC1-F5-RELATIVE`** if every exclusion recorded
  for them is REL or REL-PROD; **`LOC1-F5-PARTLY-INVARIANT`** if some is INV; **`LOC1-F5-SAMPLED`** if none is INV and
  some is INV-SAMPLED; **`LOC1-F5-OPEN`** otherwise.
- **Leg T tokens over I0:** **`LOC1-T-INV`** (some exclusion INV), **`LOC1-T-REL`** (some REL), **`LOC1-T-SPLIT`** if
  both; otherwise **`LOC1-T-ALL-INV`**, **`LOC1-T-ALL-REL`** or **`LOC1-T-UNDETERMINED`**. An INV-SAMPLED class
  contributes to none of the INV tokens; it prints **`LOC1-T-SAMPLED`** beside them.

### 7.S Leg S

- **S-I0 (coupling-degree minimization).** For each rule and decomposition `B`: `G_B = B M B⁻¹`; the coupling graph
  `i ∼ j` (`i ≠ j`) iff `G_B[i][j] ≠ 0` or `G_B[j][i] ≠ 0`; `deg_max(B)` (primary order), `e(B)` (secondary), `self(B)`.
  - On `S-edge1(α)` and `S-free`: every decomposition (owner decision (c): all 63,180, at the measured cost of §9). List
    the minimizers and group them into `C(M)`-orbits.
  - On `S-ring(q)`: the special decompositions, then 2,000 stratified samples.
  - **`LOC1-S-CRIT-FAILS`:** on some rule, some decomposition has `deg_max` strictly below the natural one's (one
    witness suffices, sampled or not). **`LOC1-S-CRIT-NONUNIQUE`:** on some enumerated rule the minimizers fall into at
    least two `C(M)`-orbits. **`LOC1-S-CRIT-HOLDS`:** neither, on an enumerated rule; on a sampled rule the same outcome
    is **`LOC1-S-CRIT-HOLDS-SAMPLED(N)`**.
- **S-I1.** On every enumerated rule, `|I1(M)|` and the minimizers within I1; whether they are the natural
  decomposition: **`LOC1-S-I1-SPATIAL`**, **`LOC1-S-I1-OTHER`** or **`LOC1-S-I1-TIED`**. On `F_q^8`, by closure.
- **S-I2 (regional independence).** On `S-free` and `S-deep`, enumerate every decomposition and bipartition and list
  the regional uncoupled assignments; on every configuration compute `Z₁`, `Z₂`, `dim(Z₁ + Z₂)`, `dim(Z₁ ∩ Z₂)`.
  - **`LOC1-S-ANCHOR-UNIQUE`** when (a) wherever `Z₁ ⊕ Z₂` is the whole dual space the assignment is unique and equals
    `(Z₁, Z₂)` (exhaustive on `S-free`; by W-OBS on `F_3^8`), (b) on `S-deep` every assignment has `span W₁ ⊇ Z₁` and
    there is more than one, and (c) on `S-cut` and `S-chain`, `Z₁ ∩ Z₂ ≠ 0`.
  - **`LOC1-S-ANCHOR-FREE`:** (a) fails while (c) holds. **`LOC1-S-ANCHOR-UNDETERMINED`:** (c) fails, so the closure test
    is not shown able to detect coupling.
  - Cross-check, reported and not a token: (b) is the linear form of the deep-sector gauge (Substratum.md:92,
    Theorem 24(iii)).

### 7.V The decisive reading

The reading separates three statements and prints only the one the tokens earn, with its scope named:

1. **Uniqueness within a class justified without the dynamics' answer** (I0 or I1): the identification is unique in
   that class on the configurations examined. Printed only from exhaustive or terminated-search cells.
2. **Uniqueness only within I2:** the identification is unique given the added regional-independence assumption,
   stated as an assumption beside the token.
3. **Non-uniqueness or relativity:** the verdicts depend on an identification the stated class does not fix.

No enumeration, search or sampling result is stated as uniqueness or invariance beyond its class and the cases
examined, and no sampled cell is stated as universal.

## 8. Controls

A token printed over a failed control is void, and the round then prints `VOID`. Budget exhaustion is never `VOID`.

**Mandatory (owner):**

| id | content |
| --- | --- |
| K-C21 | S16 finds the `τ` class for `T` (W-T) and the identity class for `P`, so REL is reachable; it finds no class for a transposition on `Fin 16` (W-CYC-16), so INV is reachable and S16 can return nothing |
| K-repro | at `σ₀`, every P0 status line (output lines 15–76) and every pair-verdict line (113–178) for `CT4`/`CCT4` and the other frozen pairs is reproduced verbatim; at leg S's natural decompositions, P2's `LS-FAC` lines are reproduced |
| K-ring | on `S-ring(3)`, re-derived and not imported: the spatial decomposition has `deg_max = 3` and 8 edges, the eigenmode decomposition `deg_max = 1` and 4 edges; the φ-pullback has the spatial graph and is a distinct decomposition; A4(b) holds spatially and fails in eigenmode coordinates |

**Scope controls (I0/I1/I2):**

| id | content |
| --- | --- |
| SC-nest | `I2 ⊆ I1 ⊆ I0` as computed, in every case; `σ₀ ∈ I1(C)` wherever `σ₀ ∈ I0(C)` |
| SC-I0 | I0 can exclude: `CENT`'s CNOT law is a non-product under every identification (W-CYC), so `I0(CENT) = ∅` is reachable; and I0 can include a non-declared class: the W-PAR class at `CCC` (K-rel-pos) |
| SC-I1 | K-hid below, and a mutation in which a carrier reads one hidden column makes K-hid fail |
| SC-I2 | the I2 conditions discriminate and admit both outcomes: on leg T, a constructed lift regionally independent under exactly one hidden class and a constructed lift regionally independent under all three (both outside the frozen lifts); on leg S, `S-cut` and `S-chain` admit no regional uncoupled decomposition, `S-free` admits one, `S-deep` more than one. A conjugate of a coupled rule by a non-monomial basis change is not made regionally independent by that conjugation |
| SC-W-I2T | for every recorded exclusion, the enumerated `I2(C, b)` is empty, as W-I2T states |

**Carried from thread B's draft rules:**

| id | content |
| --- | --- |
| K0 | exact arithmetic; the `ℚ(ζ₁₆)` self-test of P0's K0; standard library only; two runs byte-identical |
| K-cls | class counts equal W-CLS (18, 6, 3 and 1) and W-CLS-S; every `A` representative fixes the anchor; enumerated decompositions invertible and pairwise distinct |
| K-adm | every transported lift is admissible for the transported `Γ` (readback equality) |
| K-hid | W-HID: carrier values under `(σ_V, σ_A)` equal those under `(σ_V, id)`, exactly, for every lift and carrier |
| K-prod | PC accepts a constructed product and rejects `F₁₆` and P0's mutated `H₁ ⊠ H₁` |
| K-rep | the W-REP certificate agrees with an explicit product lift on two constructed instances, and its rank clause rejects a product channel with a factor of Kraus rank 4 > `|A₁|` |
| K-rel-pos | the `CCC` sweep finds the W-PAR class with `Γ` a product |
| K-search | S16, generalized to `m × n`, returns exactly the brute-force class set on `Fin 8 ≅ Fin 2 × Fin 4` (840 classes) for a seeded product relabelled by a seeded `σ*`, and recovers a planted class on `Fin 16`; a weakened pruning test and a broken symmetry breaker are each detected |
| K-sample | the stratified sampler is reproducible from its seed and its strata are the ones §9 fixes |
| K-engine | the preflight's frozen engine controls (K-canon class counts on small shapes; the brute-force replay for `N ≤ 9`; K-plant; K-perm; K-collision) and its engine and replay mutation harnesses, rerun at stage 2 |
| K-leap, K-dep | each leg-S rule's matrix equals the direct leap formula on every state; coupling graphs from the matrix pattern equal brute-force dependency over every state of each frozen decomposition on `F_3^4` and `F_3^8`, and on 2,000 seeded states on `F_5^8` |
| K-eig, K-same | the eigenmode columns are eigenvectors with the stated eigenvalues; the pullback by the site shift is the natural factorization and the φ-pullback is not (W-PB) |
| K-obs | on `S-free`, the closure assignment equals the exhaustive enumeration's unique assignment |

**Independent replay of every decisive witness.** A second script, sharing no code with the first, recomputes each
witness that decides a token — the identification, the transported operators, the product test and the verdict —
reading only the witness list the first script writes. Any disagreement voids the token.

## 9. Budget and measured costs

The owner's frozen limits: exhaustive classification up to 50,000 inequivalent identifications per case; otherwise up
to 2,000 reproducible, preferably stratified, samples per case plus targeted counterexamples, with a bounded result
reported rather than a universal one. Two decisions apply them:

- **(b) `C21`:** no unrestricted enumeration of its 18,162,144,000 classes. The pruned, symmetry-reduced complete
  search S16 runs first; only where it cannot terminate within its budget does the sampled fallback apply, reported as
  sampled.
- **(c) `F_3^4`:** a one-case exception to the 50,000 limit: all 63,180 decompositions, given the measured cost below.

| leg | case | scope sizes | method |
| --- | --- | --- | --- |
| T | `CCT4`, `CCC` | `D(C)` 18; I1 ambient 6 | exhaustive |
| T | `CENT` | `D(C)` 3; I1 ambient 1 | exhaustive |
| T | `C21` | `D(C)` 18,162,144,000; I1 ambient 1 | S16, then the sampled fallback |
| T | search-engine control | `Fin 8` as 2×4: 840 | exhaustive |
| S | `S-edge1(α)`, `S-free`, `S-deep` | `F_3^4`: 63,180 | exhaustive (exception) |
| S | `S-ring(3)`, `S-ring(5)` | `F_3^8`: 1.86 × 10²³; `F_5^8`: 1.56 × 10³⁵ | special + 2,000 stratified; I1/I2 by closure |
| S | `S-edge2`, `S-cut`, `S-chain` | > 10²³ | closure only |

**Measured at drafting.** The preflight was blinded. It evaluated only:
- synthetic instances;
- controls whose answers a written statement fixes;
- P0's admitted lift `P` at `C21`;
- counts.

No target object was evaluated. Its scripts and outputs are copied to `design/` at stage 1 (sha256 below).

- **`F_3^4`.**
  - Enumeration gives 63,180 decompositions, and an independent count that shares no code agrees.
  - Costs: enumeration takes 1–2.5 s, and a coupling graph 19–27 µs per decomposition and rule, about 1.5 s per rule.
    Peak memory is about 181 MB. The exhaustive K-dep over all 63,180 decompositions and three rules takes 151–181 s.
  - The one-case exception is affordable.
- **S16 at `C21`.**
  - The engine looks for a `σ` under which every target is a Kronecker product. It combines:
    - symmetry breaking by restricted-growth strings, one representative per class, with a lexicographic rule for the
      part swap;
    - four necessary pruning rules: support; cycle consistency, by a weighted union-find on images mod a prime; the
      W-COL family, including row and column power sums; and a partner rule;
    - a static greedy assignment order, fixed before the search;
    - an exact leaf test.
  - Its completeness proof is written out with the preflight, and W-SEP restates it.
  - Proxy runs: 114 terminated. They covered planted products in four families, joint pairs, random and near-product
    matrices, strongly regular graphs, and permutation matrices of 23 cycle types, the W-CYC-16 transposition among
    them. They needed between 16 and 1,397,548 tested nodes, with a median of 203.
  - At 3.0–47.8 µs per node, a budget of 10⁸ nodes is 5–80 minutes per run.
  - A constructed adversarial pair of matrix and order would need about 3 × 10¹⁰ nodes. So exhaustion remains possible,
    and it gives OPEN.
  - The partner rule and the greedy order were added during calibration on synthetic proxies.
- **The sampler.**
  - Stratum `k` is the largest number of points of the declared first row `{0, 1, 2, 3}` that one block of `σ`'s row or
    column partition keeps together. It is a class invariant.
  - The strata hold 239,500,800, 14,010,796,800, 3,832,012,800 and 79,833,600 classes.
  - 500 classes per stratum, 2,000 in all, are drawn from a fixed seed without replacement, in about 1.5 s.
  - Any one class is sampled with probability at most about 6 × 10⁻⁶. INV-SAMPLED(2000) therefore carries little weight
    against a rare REL witness, which is why it is never read as invariance.
- **Exact arithmetic in ℚ(ζ₁₆).** Not measured.
  - Images are taken mod a prime `p ≡ 1 (mod 16)`, with an assertion that no nonzero entry maps to 0.
  - The leaf test stays exact in ℚ(ζ₁₆).

**Rules frozen from these measurements.**
- **`F_3^4`.**
  - Every decomposition is enumerated for each rule.
  - The cell is exact iff the enumerated count, the independent count and the exhaustive K-dep all pass.
  - Any failure is VOID. There is no sampled fallback.
- **`C21`, per (lift, carrier) target set.** S16 runs in existence mode, with the frozen order and rules, under a budget
  of 10⁸ tested nodes.
  - **FOUND:** the witness goes to the independent replay, and the verdict is the replayed one.
  - **NONE within the budget:** certifies that no class exists (W-SEP).
  - **EXHAUSTED:** OPEN, with the node count.
    - It is followed by the special identifications of §5 and then the 2,000 stratified samples.
    - A replayed hit is read as REL; otherwise the class is INV-SAMPLED(N), never INV.
- **Supplementary.** Enumeration of all classes runs under its own budget and is reported as bounded if it stops early.
  No token needs it.

**Preflight files, copied to `design/` at stage 1:**

| file | sha256 |
| --- | --- |
| `c21_engine.py` | `28a6a538245a250f7e4aa80957f9e420d191a38461e3cfc02955f5da7f5dd6fc` |
| `c21_search.py` | `715270755052258ff443d5967b0fddbb655f6345d19b52f979deea435a93a0ba` |
| `c21_replay.py` | `c898a9bd628813d0641b3a1b72044d8d575aefd6dd4787d8034e4afc0f6895bd` |
| `c21_replay_mut.py` | `a4443f5ec9094049d25104a4a77aa8e817235ced6cd2b3f6cad81b059795c951` |
| `c21_sampler.py` | `c5df4f297f9d8501668cc0f6beedcbb497e70b255f1ec4f1743a5e075c2e36b8` |
| `f34_enum.py` | `594bd6a4b2cbdcddef0d52f6d9f05d17092838c25e295d8ccea808c9983b5efb` |
| `f34_count_indep.py` | `f0bc84171fb69f631b28119f3b46ed0740cbb21723f564d6e6af4d00f68ce4bd` |
| `scope_T.py` | `b0edfc9322b68c022913433ac1069419f83bedd78252199d9e7d7ebfa8e03583` |
| `frozen_inputs.json` | `89e94743d08a07c74f5a7661da7839ca7434d627acfeb9c556805fe01059c803` |
| `sizes.py` | `ab4d5ee342029a9d4907264609743762273045c58fa411d49cfc7dd3465304f1` |

Their outputs are copied with them. The scripts read nothing outside their own directory, and each was run twice with
byte-identical output.

## 10. Invariants and checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| the rules precede every run on a target | the code is frozen by blob at `F`; before `F` it runs only in control mode on non-target inputs (§12); K0 |
| the frozen witnesses and conventions are P0's and P2's | K-repro |
| identifications are complete per class | K-cls; W-CLS; K-search |
| each quotient is by relabellings only | W-REL; the centralizer is not quotiented (§3.1) |
| hidden relabelling cannot change SEP-PHYS | K-hid |
| the scopes nest and each can discriminate | SC-nest; SC-I0; SC-I1; SC-I2 |
| I2's content for recorded exclusions is fixed in advance | W-I2T; SC-W-I2T |
| SEP-REP is certified, not inferred | K-rep; W-REP |
| both INV and REL are reachable | K-C21; SC-I0 |
| the search is complete when it terminates | W-SEP; K-search; node counts reported |
| a sampled result is never read as invariance | §3.4; §7.V; K-sample |
| the coupling graphs are computed, not assumed | K-dep; K-leap |
| the closure route agrees with enumeration | K-obs |
| every decisive witness is replayed independently | the replay script |
| replayable | K0 |

## 11. Non-claims fixed in advance

- No identification, locality principle or factorization criterion is adopted.
- **Visible identifications are set-level.** Visible configurations are registered values (Lemma 1), so unitary
  re-identifications of `V` are out of scope; hidden unitaries fixing the anchor ray change no carrier value (W-HID).
- **P0's factor shapes are kept.** Other shapes could only turn OPEN into REL, never undo an INV verdict.
- **Leg S is linear.** Nonlinear decompositions and rules are out of scope.
- Coupled-cut locality within a factor (`L-disc`, `L-cont`), Bell preparations and H-Bell are out of scope.
- **Every class is a statement about the frozen configurations and recorded exclusions.** No universal claim is made,
  and a sampled class is an observation over its samples.
- The exploratory classification on record — `We.X` and `WW.Ke` invariant, `Lcc`, `Ucv` and `T`
  identification-relative — stays provisional until these cells decide it; the round does not use its tokens.
- Written statements are not kernel proofs.
- Nothing says how nature identifies its parts, or whether `SL-U` holds in nature.
- Correctness bands are unchanged: this is consistency work (§A.23).

## 12. Stages and outcomes

- **Before `F`:** the round's code — the run script, the independent replay script and `controls.py` — is written and
  its blobs are recorded here. It is exercised only in control mode, on the synthetic and written-answer inputs of §8,
  locally and on a disposable branch at the predicted tree (design evidence, not attestations). The `F` check run is
  dispatched with the branch held at exactly `F`, before the designation record is posted, and no execution commit is
  made before that record.
- **Stage 1:** the ported objects (`objects/`, proposed (f)), the disclosed prior scripts and outputs (`prior/`, §13), the
  drafting-time cost measurements of §9 (`design/`), and the code, each at its frozen blob. After stage 1 every file the
  round cites is in its record directory or on `main`; nothing it relies on is a scratch file or a branch other than
  `main`.
- **Stage 2:** the run, twice, byte-identical; the replay; the outputs and the witness list as record files.
- **Stage 3:** the result note, its tokens printed from the outputs, with the proofs of §6.
- **`E`:** the exact-head run at `E` is dispatched before `E` is designated. Then reconciliation, the receipt `Q` and
  `tools/v3_verifier.py --verify-round Q`.

**What voids the round:** a failed control of §8; a departure from P0's or P2's frozen conventions found by K-repro; a
difference between two runs; a disagreement with the independent replay.

## 13. Prior knowledge disclosed

The cells were chosen with the following knowledge. **None of these results is used as a token.** Each script and
output named below is copied into the record directory at stage 1 (`prior/`), pinned by its sha256 here, so that this
disclosure points to content retained with the round; until then the names identify working material, not evidence.

- **Thread B's exploratory sweep** (`explore/decomposition_probe.py`, sha256 `acdd998d…`, output `f32b7f82…`), exact
  with green controls, over the 3 × 3 identifications at `CCT4` and `CCC` and the three at `CENT`: `Lcc` on `𝒪₁`
  SEP-PHYS in the three identifications that keep the declared `V`-class and SEP-REP in the other six; `We.X` SEP-PHYS
  on all three carriers in all nine; `WW.Ke` SEP-PHYS on `𝒪₂` and `𝒪₃` in all nine; `CCC`'s `Γ` a product in six of
  nine, with `Ucv` SEP-REP there; `CN` a non-product in all three. Its SEP-REP certification used hand-built product
  lifts; these rules replace it with W-REP and keep two of those lifts only as the K-rep control.
- **The four-site countermodel** (#851's check, script sha256 `52694d4a…`, output `9ef260e7…`): on `S-ring(3)` the
  natural factorization has `deg_max = 3` and 8 edges and the eigenmode one `deg_max = 1` and 4 edges; the φ-pullback
  has the natural graph and is distinct. These are K-ring's numbers, which the round re-derives.
- **Thread B's closure design** (`explore/closure_design.py`, sha256 `bb33939e…`, output `88921a99…`): on `U-free(3)` and
  every `U-edge(3, α, β)`, `Z₁ ⊕ Z₂` is the whole space and equals the natural regional spans; on `C-cut`, `C-chain` and
  a single coupled edge, `Z₁ ∩ Z₂ ≠ 0`.
- **Known before any computation:** W-T, by the construction of `T`; W-I2T; and that leg S's anchor result is close to a
  theorem (W-OBS) under P2's register convention, which is why `S-deep` and `S-edge2-sparse` are included.
- **The drafting preflight** (§9) evaluated no target object. Three of its facts are disclosed:
  - Thread B's exploratory sweep counted 9 identification classes at `CCT4` and `CCC`, because it quotiented `V` and `A`
    separately, each with its own factor swap. That identifies each pair of the 18 classes defined here, so the sweep
    evaluated one class of each pair.
  - The complete enumeration for P0's admitted lift `P` at `C21` ends with 10 classes under which `P` is a product. That is
    a fact about an admitted lift, and it bears only on the supplementary reverse direction.
  - S16's partner rule and its greedy order were tuned on synthetic proxies.

## 14. Owner decisions

**Made on 2026-10-16:**

- **The scopes.** I0, I1 and I2 as §1 states them; for I2, requiring the same abstract dynamics up to coordinate
  conjugacy is insufficient, so the condition must have discriminating content (§3.2, SC-I2). No enumeration or sampling
  result is promoted into an unrestricted uniqueness theorem (§7.V).
- **The budget** and the mandatory controls `C21`, `CT4` and the four-site countermodel (§8, §9).
- **(b) `C21`:** no unrestricted enumeration; mathematically justified pruning and symmetry reduction first; if
  exhaustive coverage cannot be proved, up to 2,000 reproducible, preferably stratified samples plus targeted
  counterexamples, reported as sampled, not universal (§7.T, §9).
- **(c) `F_3^4`:** a one-case exception to the 50,000 limit, exhausting all 63,180 if the measured cost is acceptable
  (§9).
- **(d) Leg T I2:** to be marked not applicable only if its formal domain genuinely excludes T, with the precise
  reason; if meaningful but untested, unresolved. **Applied:** I2's formal domain does not exclude leg T. Its natural
  dynamical condition, regional independence of the lift, is `SL-U`'s own admission criterion, so I2 is meaningful
  there. Its content for every recorded exclusion is fixed in advance by W-I2T (empty), and its measured content is the
  number of hidden identifications under which each admitted lift is regionally independent. The cell is cheap and
  exhaustive (at most six classes per configuration), so it is **tested** (T-I2) rather than marked unresolved. If
  the owner prefers not to test it, it is marked unresolved with this reason.
- **Proven versus observed invariance** are separate tokens (§3.4).

**Still the owner's, with the proposed option carried in this draft:**

- **(a) I0 for leg T.** *Proposed:* "compatible with the visible law" as `Γ^σ` a product, which is what makes `SL-U`
  applicable. *Alternative:* `Γ^σ = Γ` exactly, the symmetries of the visible law; stricter, and at `C21`, where
  `Γ ≡ 1/16`, it coincides with the proposed reading.
- **(e) Label, placement and kind.** *Proposed:* `LOC-1`; record directory
  `verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/`; non-sealing; the P0 and P2 research
  records cited as provenance and not edited.
- **(f) The frozen objects.** P0's and P2's live on research branches, not on `main`, and a record may not rest on
  content outside `main` (owner rule of 2026-10-16), so citing the research commits alone is not an option.
  *Proposed:* port the frozen configurations, lifts and conventions into `objects/` at stage 1, with their blobs and
  the research commits they come from recorded as provenance, and checked by K-repro. *Alternative:* land those research
  records on `main` first, by a separate decision.
