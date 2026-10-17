# Locality round LOC-1 — how locality verdicts depend on the identification of parts: PREREGISTRATION (draft)

**Status: drafting, native V3; not a candidate `F`.** Drafted on a pull request from `D` for owner review. The owner's
design decisions of 2026-10-16, (a) to (f), are applied (§14); the choices §14 marks "(proposed)" await the owner's
decision. Nothing is executed. No workflow is dispatched for this round, and its code is not run on any target object
before `F`. Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round LOC-1
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/
record A verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/objects/
record A verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/design/
record A verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/prior/
record A verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/retained/
record AM verification/receipts/LOC-1.json
```

The `objects/`, `design/`, `prior/` and `retained/` entries admit additions only. Stage 1 adds the copies of §2.1, the
design files of §9 and the prior files of §13; the first execution commit adds `retained/F/` (§12). No later commit of
the round modifies or deletes any of them.

D: fc5abade2a8ca381caedaa93c0441570fc060319, `main` after #851, #849 and #850. The round relies on two properties of
`D`, both read from the repository: `D` is an ancestor of `F`, and `D` lies on the first-parent chain of every
reconciliation's first parent (K3).
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory. **No manuscript, built
artifact, module, census entry, probe, workflow, coverage-ledger entry or research record outside the record directory
changes under any outcome.** The P0 and P2 research records are cited as provenance and are not edited. The round
depends on one change outside its own commits: `E`'s evidence-retention pull request (§12), which lands on `main`
separately and adds `retained/E/` and the evidence-retention archive's `coverage.later` entry for this round's receipt.

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
| P0's definitions: carriers `𝒪₁`–`𝒪₃`, `SL-U`, PC, RL, the frozen lifts and conventions | P0 `RULES.md` and `p0_exact.py`, copied to `objects/p0-subsystem-locality/` (§2.1) | research record, frozen |
| P0's recorded statuses and pair verdicts | P0 `p0-exact-output.txt`, copied to `objects/p0-subsystem-locality/` (§2.1), lines 15–76 and 113–178 | research record |
| P0's `NS-WEAKER` witnesses `CCT4:Lcc`, `CCT4:WW.Ke`, `CCC:Ucv`, which T-F5 reads | the same file, line 247 (`P0-NS-WEAKER  witnesses: CCT4:Lcc, CCT4:WW.Ke, CCC:Ucv`) | research record |
| P2's configurations and register convention | P2 `RULES.md`, §3–§4, and `p0_ls_exact.py`, copied to `objects/p0-locality-sources/` (§2.1) | research record |
| P2's recorded `FAC` check, cell and token, which K-repro reproduces | P2 `p0-ls-exact-output.txt`, copied to `objects/p0-locality-sources/` (§2.1), lines 4, 23 and 31: the three lines of the file that contain `FAC` (`PASS FAC`, `CELL FAC`, `TOKEN LS-FAC`) | research record |
| the cone consumes site factorization and a neighbourhood function only | `iterate_dependsOnlyOn_ball`, RegionTower.lean:283 (at `D`) | kernel theorem |
| visible configurations are registered values of a finite set | Main.md:48 (Lemma 1) | lemma |
| deep sectors decoupled from the boundary are gauge | Substratum.md:92, Theorem 24(iii) | cross-check only (§7.S) |

P0's and P2's research commits are not reachable from `main`, so they are provenance only (AGENTS §A.42). Stage 1
copies every object of theirs that the round reads into `objects/`, byte for byte, as §2.1 lists (owner decision (f)).
The round reads those objects only from `objects/`, and K-obj checks every copy before any cell runs. Not adopted, and
used only as objects of test: any identification principle, `SL-U`, coupling-degree minimization and regional
independence. None of them is a premise of the round.

### 2.1 Frozen objects copied at stage 1

Each row is one file. Its copy is `objects/<copy>`; its source is the file at
`verification/programmes/oi-qm/track-b/research-planning/<copy>` in the source commit's tree. The blob id, size and
sha256 are those of that source file, read from git (`git cat-file -s` and `git cat-file blob <blob> | sha256sum`), and
`git rev-parse <commit>:<source path>` returns the blob id shown. Each copy is byte-identical to its source, so the git
blob id is recomputable from the copy's bytes alone, without the source commit.

| copy | source commit | blob | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `p0-subsystem-locality/RULES.md` | `55450d571fe34112b5ed899052b9c97f0e2cda70` | `988b4fe218dcf014f91e0f883c56dd4a3bc2a1a0` | 26081 | `6f9493eed23652b7979333b09e1bbc3148a67ef10816ebfe2cf1ded59c3ec0df` |
| `p0-subsystem-locality/p0_exact.py` | `55450d571fe34112b5ed899052b9c97f0e2cda70` | `85251bb2d9fa7542d0c7cf9d94b423692d1d23a4` | 34224 | `00cb032b71dce6eb994864e8e18bf6748192f38a644898a9c3685d453ecd155c` |
| `p0-subsystem-locality/p0-exact-output.txt` | `55450d571fe34112b5ed899052b9c97f0e2cda70` | `b34eb9535a3d9bfed5cf94fe5388f6456afa43e4` | 14432 | `14428b8dd5e6008eb06bbe0e5516f05a570da056c3c9a6b20889a21f9fd58701` |
| `p0-locality-sources/RULES.md` | `ea9a6b71e46d01f6bca7342b9f9fd6aa7f41bfef` | `d0b286ead9f7c039b3a9d8ea6dcd36b0627a457c` | 11530 | `7fe248c2fc5289c18853ff34ef98f5d64b62b05a71ad55bfe3ae00e0af7facd3` |
| `p0-locality-sources/p0_ls_exact.py` | `ea9a6b71e46d01f6bca7342b9f9fd6aa7f41bfef` | `41905335b4f35ad7b2c10bb0cbe1951f918c70c4` | 22020 | `904e242ea52f3ddbd2462ed72dd6edd6f739737f404e9c3b517aefe19eceadf2` |
| `p0-locality-sources/p0-ls-exact-output.txt` | `ea9a6b71e46d01f6bca7342b9f9fd6aa7f41bfef` | `354edb3f6152d93a6e3a3e094e1c9da93cc25a77` | 3069 | `880c29049a8b174b12cfd73b16c8852703e319e9e9dc432247e6bc6832194813` |

Provenance: `55450d57` is a commit of branch `plan/p0-evolution-source-20261013` (#834), and `ea9a6b71` a commit of
branch `research/p2-locality-sources-20261015`; `ea9a6b71` descends from `55450d57` and carries P0's three files with
the same blob ids. The two output files hold the recorded lines that K-repro compares with the round's own
regeneration, at `σ₀` for P0 and at the natural decompositions for P2. No other file of either research record is
copied, and no cell reads one.

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

- **I0(C)** (owner decision (a)) is the set of `σ ∈ D(C)` with `Γ^σ` a product, by PC on P0's `cut_stoch`: the
  visible law is the law of two uncoupled parts in `σ`, which is what `SL-U` needs in order to apply at all. This is
  the broader factorization test; the symmetries of the visible law, `Γ^σ = Γ`, are not the scope.
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

| config | lifts | recorded exclusions (P0 output, blob `b34eb9535a3d9bfed5cf94fe5388f6456afa43e4`) | `D(C)` classes |
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

Proofs go in the result note, except W-SEP's, which is `design/S16-completeness.md` (§9). Each is checked where §8
says.

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
- **W-COL.** If `M^σ = M¹ ⊗ M²`, then each product-form function of the index, read on the grid through `σ`, is
  `u(a) v(b)`: it has rank at most 1 and product support (no zero with a nonzero in its grid row and one in its grid
  column). The product-form functions S16 uses are each column and each row of `M`, its diagonal, and the number of
  nonzeros, the sum and the sum of squares of each row and each column. These are necessary conditions on `σ` alone.
- **W-SEP** (completeness of S16), argued in full in `design/S16-completeness.md` (§9) [W]. Restricted-growth strings
  along the static order, with the lexicographic rule for the part swap, leave exactly one representative per class
  (W-CLS). Each pruning rule rejects a partial assignment only when no completion makes every target a product: support
  (N1) and cycle consistency (N2) follow from the rank-1 form of the reshuffle, the partner rule (N4) from the nonzero
  entries that form forces, and the W-COL family (N3) from W-COL. N2's images modulo `2⁶¹ − 1` reject no consistent
  system. The leaf test is PC, exact. So a run that ends within its budget has reached every class's representative:
  NONE certifies that no class exists, and an enumeration lists every class once. The argument covers integer entries,
  which is all the engine as measured accepts. For `ℚ(ζ₁₆)` entries it holds for an arithmetic layer meeting conditions
  E1–E4 of that file, which K-arith-16 checks (§8).
- **W-PB.** For `X ∈ C(M)`, `G_{BX} = G_B`; with `B = M` (the φ-pullback), `G_M = M`. The φ-pullback is the same
  factorization as the natural one iff `M` is monomial.
- **W-OBS.** A regional uncoupled decomposition has `span W_k ⊇ Z_k`, so one exists only if `Z₁ ∩ Z₂ = 0`. If
  `Z₁ ⊕ Z₂` is the whole dual space, the assignment is unique and equals `(Z₁, Z₂)`. If it is a proper subspace, the
  unobservable complement can be assigned in more than one way and influences no register.

## 7. Cells and decision rules

All arithmetic is exact: `Fraction`; P0's `ℚ(ζ₁₆)` class, from its copy in `objects/` (§2.1), for `C21`; integers mod
`q` for leg S. At `C21` the S16 engine reaches that class through an arithmetic layer meeting E1–E4 of
`design/S16-completeness.md`: exact zero tests, N3 products and leaf test in `ℚ(ζ₁₆)`, and N2 on images under a ring
homomorphism to `F_p`, `p ≡ 1 (mod 16)`, with an assertion that no nonzero entry has image 0. The independent replay
uses its own implementation of `ℚ(ζ₁₆)` (§8). Every token prints from measurements. The decision rules fix what each
measurement decides; they fix no expected number.

### 7.T Leg T

- **T-I0, at `CCT4`, `CCC`, `CENT`:** for every recorded exclusion and every `σ ∈ D(C)`, compute `Γ^σ`'s product status
  and the verdict of §3.3, then the class of §3.4 over I0(C). Exhaustive.
- **T-I0, at `C21`:** by the search S16 (below), per lift and recorded carrier. Targets: for `𝒪₁`, `U₀` and `U₁`
  together; for `𝒪₃`, `U₁U₀ᴴ` and `U₀U₁ᴴ` (W-EQ1u); for `𝒪₂`, `R(1,0)` and `R(0,1)`.
  - **S16:** the engine of `design/c21_engine.py` with rules `RWVP`. It assigns the indices along a static order fixed
    from the targets before the search (the greedy order, §9); the first index of the order goes to `(0,0)`. Symmetry
    is broken by requiring both coordinate sequences along the order to be restricted-growth strings and, for the part
    swap, the first to precede the second lexicographically; this leaves exactly one representative per class, so the
    representatives found are pairwise inequivalent without deduplication (W-SEP). After each assignment the rules
    N1–N4 (support, cycle consistency, the W-COL family, partner) are applied to every target on the known entries; at a
    complete assignment PC is applied to every target, exactly.
  - **Budget (owner decision (b)):** no unrestricted enumeration. A node budget per (lift, carrier), fixed in §9 from
    the measured node counts. **Termination** gives an exact class: INV, REL or REL-PROD, within the scope of W-SEP.
    **Exhaustion** gives the fallback:
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
- **T-F5** (P0's NS-WEAKER witnesses `Lcc`, `WW.Ke`, `Ucv`, P0 output line 247), over I0: **`LOC1-F5-RELATIVE`** if every exclusion recorded
  for them is REL or REL-PROD; **`LOC1-F5-PARTLY-INVARIANT`** if some is INV; **`LOC1-F5-SAMPLED`** if none is INV and
  some is INV-SAMPLED; **`LOC1-F5-OPEN`** otherwise.
- **Leg T tokens over I0:** **`LOC1-T-INV`** (some exclusion INV), **`LOC1-T-REL`** (some REL), **`LOC1-T-SPLIT`** if
  both; otherwise **`LOC1-T-ALL-INV`**, **`LOC1-T-ALL-REL`** or **`LOC1-T-UNDETERMINED`**. An INV-SAMPLED class
  contributes to none of the INV tokens; it prints **`LOC1-T-SAMPLED`** beside them.

### 7.S Leg S

- **S-I0 (coupling-degree minimization, an object of test here, not a premise).** For each rule and decomposition
  `B`: `G_B = B M B⁻¹`; the coupling graph `i ∼ j` (`i ≠ j`) iff `G_B[i][j] ≠ 0` or `G_B[j][i] ≠ 0`; `deg_max(B)`
  (primary order), `e(B)` (secondary), `self(B)`.
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
| K-repro | at `σ₀`, every P0 status line (output lines 15–76) and every pair-verdict line (113–178) for `CT4`/`CCT4` and the other frozen pairs is reproduced verbatim; at leg S's natural decompositions, P2's lines 4, 23 and 31 (§2) are reproduced |
| K-obj | owner decision (f): before any cell runs, `objects/` holds exactly the six files of §2.1, and each file's size, sha256 and git blob id, computed from its bytes, equal its row; the run reads P0's and P2's objects from `objects/` and from nowhere else |
| K-design | (proposed, §14 (g)) before any cell runs, `design/` holds exactly the files of §9's table, and each file's size and sha256, computed from its bytes, equal its row |
| K-prior | (proposed, §14 (g)) before any cell runs, `prior/` holds exactly the six files of §13's table, and each file's size and sha256, computed from its bytes, equal its row |
| K-arith-16 | (proposed, §14 (k)) on the S16 engine's `ℚ(ζ₁₆)` layer, before it runs on a target: E1–E4 of `design/S16-completeness.md` hold; `ρ` is a ring homomorphism on `ζ⁸ = −1` and on seeded sums and products; on seeded synthetic `ℚ(ζ₁₆)` instances (planted products relabelled by a seeded `σ*`, near-products, non-products) enumeration returns the same class sets with N2 exact and on images; an entry changed by `ζ − ω ∈ ker ρ` passes every image test at its planted leaf and is rejected by the exact leaf test; and the assertion `ρ(x) ≠ 0` holds for every entry of every `C21` target |
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
| K-engine | the preflight's frozen engine controls (K-canon class counts on small shapes; the brute-force replay for `N ≤ 9`; K-plant; K-perm; K-collision) and its engine and replay mutation harnesses, rerun at stage 2 on the frozen integer engine and on the engine with its `ℚ(ζ₁₆)` layer. On the integer engine the rerun follows the recipe of `design/preflight-expected.json`, and the regenerated outputs and expected result equal their §9 rows byte for byte |
| K-leap, K-dep | each leg-S rule's matrix equals the direct leap formula on every state; coupling graphs from the matrix pattern equal brute-force dependency over every state of each frozen decomposition on `F_3^4` and `F_3^8`, and on 2,000 seeded states on `F_5^8` |
| K-eig, K-same | the eigenmode columns are eigenvectors with the stated eigenvalues; the pullback by the site shift is the natural factorization and the φ-pullback is not (W-PB) |
| K-obs | on `S-free`, the closure assignment equals the exhaustive enumeration's unique assignment |

**Independent replay of every decisive witness.** A second script, sharing no code with the first, recomputes each
witness that decides a token — the identification, the transported operators, the product test and the verdict —
reading only the witness list the first script writes. Any disagreement voids the token. (Proposed, §14 (j).) The
replay imports nothing from `objects/`, the run script or `controls.py`:

- it implements its own exact `ℚ(ζ₁₆)` arithmetic, on the power basis `1, ζ, …, ζ⁷` over `Fraction` with
  `ζ⁸ = −1`, and its own integers mod `q` for leg S;
- it rebuilds every frozen lift it replays from its closed form in P0 `RULES.md` (§2.1), lines 197–245, under P0's index
  convention (composite index `(i₁ d₂ + i₂) n + a₁ n₂ + a₂`, factor index `i n_k + a`, anchor index 0), and every leg-S
  rule matrix from P2 `RULES.md` §3–§4 or §4.S above. It requires each rebuilt matrix to equal the one the witness list
  carries, exactly (K-replay-lifts); a difference voids the token.

Its independence therefore extends to the arithmetic, the lifts and the rule matrices, not only to the transport, the
product test and the verdict.

**Retention (AGENTS §A.42; proposed, §14 (h)):**

| id | content |
| --- | --- |
| K-ret-F | before any cell runs, `retained/F/` holds `check-run.json`, `jobs.json` and `designation.json` as §12 specifies, each well formed and naming `F`'s object id; `check-run.json` names the run, the job, the recipe and the sha256 of the text it was read from |
| K-ret-E | before `Q` is built: the evidence-retention commit reached `main` through its own pull request and is an ancestor of `LB`; at `Λ`, `retained/E/` holds the same three files for `E`, each well formed and naming `E`'s object id; the receipt's candidate entry for `E` names each of them with its sha256, and each digest matches its file; the evidence-retention archive's `coverage.later` at `LB` names `verification/receipts/LOC-1.json` with this record directory's `retained/`; and `check_retention.py`, plain and with `--later-provenance`, passes on `Q`'s tree |

A failed K-design or K-prior voids the round. A failed K-ret-F stops the run before any cell. A failed K-ret-E stops the
round before `Q`; it is repaired by a further evidence-retention pull request and a new reconciliation (S10). After `E`
the record directory changes only through the reconciliation base, never by a commit of the round.

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

No target object was evaluated. Its scripts, their outputs, the expected result read from those outputs and the S16
argument are copied to `design/` at stage 1 (the table below). Each figure below is a deterministic count, frozen as
part of the expected result `design/preflight-expected.json`, unless it is marked "observed": an observed duration
varies between runs, is not retained, and freezes nothing.

- **`F_3^4`.**
  - Enumeration gives 63,180 decompositions, `|GL(4,3)| / (4! · 2⁴)` with `|GL(4,3)| = 24,261,120`. An independent
    count that shares no code agrees: 1,516,320 ordered independent 4-tuples of the 40 points of `PG(3,3)`, divided by
    `4!`.
  - The exhaustive K-dep compares the coupling graph of each of the 63,180 decompositions with brute-force dependency,
    for three rules, with 0 mismatches; the default run compares 1,966 seeded decompositions for the same three rules.
  - Observed: enumeration 1.1–2.2 s; coupling graphs 22–34 µs per decomposition and rule; the exhaustive K-dep
    151–208 s; peak memory about 182 MB.
  - The one-case exception is affordable: its cost is the 63,180 × 3 comparisons of the exhaustive K-dep, which
    completed in each of its three runs.
- **S16 at `C21`.**
  - The engine looks for a `σ` under which every target is a Kronecker product. It combines:
    - symmetry breaking by restricted-growth strings, one representative per class, with a lexicographic rule for the
      part swap;
    - four necessary pruning rules: support (N1); cycle consistency (N2), by a weighted union-find on images modulo the
      prime `2⁶¹ − 1`; the W-COL family (N3), including row and column power sums; and a partner rule (N4);
    - a static greedy assignment order, fixed before the search;
    - an exact leaf test.
  - Its completeness is argued in `design/S16-completeness.md` [W], which W-SEP restates. The argument covers integer
    entries, the only entries the engine as measured accepts. At `C21` it applies through the `ℚ(ζ₁₆)` layer of §7,
    checked by K-arith-16.
  - Proxy runs in existence mode, at the frozen rules and order: 114 terminated, 48 FOUND and 66 NONE. They covered
    planted products in four families, joint pairs, random and near-product matrices, strongly regular graphs, and
    permutation matrices of 23 cycle types, the W-CYC-16 transposition among them (NONE at 64,079 tested nodes). They
    needed between 16 and 1,397,548 tested nodes. The script's median, the 58th of the 114 sorted counts, is 203; the
    57th is 200. P0's `P` is FOUND at 16 tested nodes.
  - Three further existence runs, each in a configuration other than the frozen one (the natural order, or the partner
    rule removed, or both), exhausted a cap of 2 × 10⁶ tested nodes on the near-identity matrix `I + E₁₄,₁₅`, which the
    frozen order and rules decide NONE at 63,987 tested nodes. Seeded Knuth estimates put the natural-order tree at
    about 3.1 × 10¹⁰ tested nodes. The tree size depends on the target and on the order, so exhaustion of the frozen
    budget remains possible; it gives OPEN.
  - The partner rule and the greedy order were added during calibration on synthetic proxies.
  - Observed: about 3 to 58 µs per tested node at the frozen rules and order, across the drafting runs (16-point
    proxies with at least 1,000 tested nodes).
- **The sampler.**
  - Stratum `k` is the largest number of points of the declared first row `{0, 1, 2, 3}` that one block of `σ`'s row or
    column partition keeps together. It is a class invariant.
  - The strata hold 239,500,800, 14,010,796,800, 3,832,012,800 and 79,833,600 classes, 18,162,144,000 in all.
  - 500 classes per stratum, 2,000 in all, are drawn from a fixed seed without replacement, in 112,150 draws. The sample
    list's sha256 is `6f1d6b6d4db6fb8db02d6922cea9052e29edf1d9836a5066f8395295a2bc2b13`, the digest of
    `c21_samples.json`. Observed: about 1.3 s.
  - Any one class is sampled with probability at most 500 / 79,833,600, about 6.3 × 10⁻⁶. INV-SAMPLED(2000) therefore
    carries little weight against a rare REL witness, which is why it is never read as invariance.
- **Exact arithmetic in ℚ(ζ₁₆).** Not measured: the engine as measured converts every entry to an integer. The layer of
  §7 is part of the round's run script, written before `F`, and K-arith-16 checks it.

**Rules frozen from these measurements.**
- **`F_3^4`.**
  - Every decomposition is enumerated for each rule.
  - The cell is exact iff the enumerated count, the independent count and the exhaustive K-dep all pass.
  - Any failure is VOID. There is no sampled fallback.
- **`C21`, per (lift, carrier) target set.** S16 runs in existence mode, with the frozen order and rules, under a budget
  of 10⁸ tested nodes. The budget rests on the deterministic counts above: it is more than 71 times the largest
  terminated proxy run (1,397,548 tested nodes) and about 4.9 × 10⁵ times the median (203), and it lies below the
  3.1 × 10¹⁰ estimate for the adversarial order, so exhaustion is not excluded. No duration enters the rule.
  - **FOUND:** the witness goes to the independent replay, and the verdict is the replayed one.
  - **NONE within the budget:** certifies that no class exists (W-SEP, within its scope).
  - **EXHAUSTED:** OPEN, with the node count.
    - It is followed by the special identifications of §5 and then the 2,000 stratified samples.
    - A replayed hit is read as REL; otherwise the class is INV-SAMPLED(N), never INV.
- **Supplementary.** Enumeration of all classes runs under its own budget and is reported as bounded if it stops early.
  No token needs it.

**Files copied to `design/` at stage 1.** Each row is one file. Its copy is `design/<file>`, byte-identical to the
working file pinned here; K-design checks every copy against its row.

| file | role | form | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `c21_engine.py` | S16 engine | complete | 21164 | `28a6a538245a250f7e4aa80957f9e420d191a38461e3cfc02955f5da7f5dd6fc` |
| `c21_search.py` | S16 proxy suite, its controls and the engine mutation harness | complete | 24216 | `715270755052258ff443d5967b0fddbb655f6345d19b52f979deea435a93a0ba` |
| `c21_replay.py` | independent replay of the search witnesses | complete | 7143 | `c898a9bd628813d0641b3a1b72044d8d575aefd6dd4787d8034e4afc0f6895bd` |
| `c21_replay_mut.py` | replay mutation harness | complete | 2061 | `a4443f5ec9094049d25104a4a77aa8e817235ced6cd2b3f6cad81b059795c951` |
| `c21_sampler.py` | stratified sampler of `C21` classes | complete | 7502 | `c5df4f297f9d8501668cc0f6beedcbb497e70b255f1ec4f1743a5e075c2e36b8` |
| `f34_enum.py` | `F_3^4` enumeration, coupling graphs and K-dep | complete | 14346 | `594bd6a4b2cbdcddef0d52f6d9f05d17092838c25e295d8ccea808c9983b5efb` |
| `f34_count_indep.py` | independent count of `F_3^4` decompositions | complete | 2439 | `f0bc84171fb69f631b28119f3b46ed0740cbb21723f564d6e6af4d00f68ce4bd` |
| `scope_T.py` | leg-T scope sizes | complete | 4812 | `b0edfc9322b68c022913433ac1069419f83bedd78252199d9e7d7ebfa8e03583` |
| `frozen_inputs.json` | P0's `H₁` (times 2) and index convention, read by `c21_search.py` | complete | 637 | `89e94743d08a07c74f5a7661da7839ca7434d627acfeb9c556805fe01059c803` |
| `sizes.py` | scope sizes against the frozen limits | complete | 2106 | `ab4d5ee342029a9d4907264609743762273045c58fa411d49cfc7dd3465304f1` |
| `sizes.out` | stdout of `sizes.py` | complete-as-cited | 1350 | `558bce27933c552d87dfc555bad043943296c3005d67e5c53614d8ea726e91fe` |
| `scope_T.out` | stdout of `scope_T.py` | complete-as-cited | 631 | `5f046ca1a24caa8c021d6a495b27293ffaee5f90655f90851752abc6d90625da` |
| `f34_count_indep.out` | stdout of `f34_count_indep.py` | complete-as-cited | 208 | `89253e0df60bae63193c6107ec57b0ead21bbd358fafdaf116154adf9dd1c2ac` |
| `f34_enum.out` | stdout of `f34_enum.py` | complete-as-cited | 2537 | `93704f647192cd2f00bee30a2ddd4879e831aa18029558d67efa0000cbbd7128` |
| `f34_enum_kdepall.out` | stdout of `f34_enum.py --kdep-all` | complete-as-cited | 2537 | `72485aef26438ddf08ce1fb1833d8bf5f63cfa6fcdd6d6eb157fe6061a5a1701` |
| `c21_search.out` | stdout of `c21_search.py`; its line positions are cited | complete-as-cited | 54521 | `f09b4840c2471d27ab601a7029fd3bce07cd17c921da8b79ce44fb3350010a9d` |
| `c21_witness.json` | witness list written by `c21_search.py`, read by the replay | complete-as-cited | 1912475 | `eca55c800cf6f19a5fb25cd586b8af43ac2ad0b5942b8c7f81b517a1e9866f15` |
| `c21_replay.out` | stdout of `c21_replay.py` | complete-as-cited | 178 | `d254d7cc2ca244a62aab0002918b680b13569f315a12593eec41fd39f10cc011` |
| `c21_replay_mut.out` | stdout of `c21_replay_mut.py` | complete-as-cited | 391 | `1b69431f3e63ded08410197935a6c48c746b58bf445927020a47b710a195f19c` |
| `c21_sampler.out` | stdout of `c21_sampler.py` | complete-as-cited | 1021 | `b61c10fa25c9aa056e80fbc38967fab0a62b874b16dcd0bd75d73371c86eacbc` |
| `c21_samples.json` | sample list written by `c21_sampler.py` | complete-as-cited | 88001 | `6f1d6b6d4db6fb8db02d6922cea9052e29edf1d9836a5066f8395295a2bc2b13` |
| `preflight_expected.py` | extractor of the expected result | complete | 13458 | `16a9fcbb0f823da2765bb770962c67782f1db888aea31167876cc3fad5a814f4` |
| `preflight-expected.json` | expected result: the deterministic content of the eleven outputs above | derived | 26358 | `70a1e1eda648d78b56b5b446285c66b8deeaf6d8a65412cc56c42cbbeca178ac` |
| `S16-completeness.md` | the S16 completeness argument | complete, [W] | 15937 | `d45ae28ab475745ad2125fa9b05cf49229adf52a2a96c2caeace62741a40ca36` |

- **Runs.** Each output in the table was produced three times, in separate copies, byte for byte the same. For every
  output but `f34_enum_kdepall.out`, the three runs are the two drafting runs and a run of the whole set in a fresh
  copy, all on 2026-10-16. `f34_enum.py --kdep-all` was not part of the second drafting run; its three runs are the
  first drafting run, that fresh-copy run, and a run in a further fresh copy on 2026-10-17.
- **Timings.** The scripts write their timings to stderr, which differs between runs. Stderr is not copied, and nothing
  is frozen from it.
- **Inputs.** The scripts import the standard library and, for `c21_search.py`, `c21_engine.py` only;
  `c21_replay_mut.py` runs `c21_replay.py` as a subprocess. They read nothing outside their own directory, except the
  temporary files `c21_replay_mut.py` writes and hands to `c21_replay.py`.
- **The expected result.** `preflight_expected.py` regenerates `preflight-expected.json` byte for byte from each of the
  three output sets. The file names its sources by sha256 and the recipe that regenerates them.
- **Scope counts.** `sizes.out` lists `CCT4` and `CCC` at 9 classes, under thread B's set quotient (§13). The round's
  counts are those of `scope_T.out` under the quotient of §3.1: 18 classes and an I1 ambient of 6.
- **Design runs (proposed, §14 (h)).** Each disposable-branch design run that §12 cites is retained as an expected
  result `design/runs/<run>.json`, in the form of `retained/F/check-run.json` (§12). Its row is added to this table,
  with its size and sha256, before `F`, and the file is copied at stage 1.

## 10. Invariants and checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| the rules precede every run on a target | the code is frozen by blob at `F`; before `F` it runs only in control mode on non-target inputs (§12); K0 |
| the frozen witnesses and conventions are P0's and P2's | K-repro |
| the objects the round reads are P0's and P2's frozen files, byte for byte | K-obj, against §2.1's sizes, sha256 digests and blob ids, frozen at `F`; `objects/` is add-only (`v3-governed-paths`) |
| identifications are complete per class | K-cls; W-CLS; K-search |
| each quotient is by relabellings only | W-REL; the centralizer is not quotiented (§3.1) |
| hidden relabelling cannot change SEP-PHYS | K-hid |
| the scopes nest and each can discriminate | SC-nest; SC-I0; SC-I1; SC-I2 |
| I2's content for recorded exclusions is fixed in advance | W-I2T; SC-W-I2T |
| SEP-REP is certified, not inferred | K-rep; W-REP |
| both INV and REL are reachable | K-C21; SC-I0 |
| the search is complete when it terminates | W-SEP, argued in `design/S16-completeness.md`; K-search; K-engine; node counts reported |
| at `C21` the search's arithmetic meets E1–E4 of that argument | K-arith-16; K-engine on the extended engine |
| a sampled result is never read as invariance | §3.4; §7.V; K-sample |
| the coupling graphs are computed, not assumed | K-dep; K-leap |
| the closure route agrees with enumeration | K-obs |
| every decisive witness is replayed independently | the replay script, with its own `ℚ(ζ₁₆)` arithmetic and its own lifts (K-replay-lifts) |
| replayable | K0 |
| the preflight's ten scripts and inputs are the pinned files | K-design, against §9's table; `design/` is add-only (`v3-governed-paths`) |
| the preflight's eleven outputs are the pinned files and are deterministic | K-design; K-engine's byte-for-byte regeneration at stage 2 |
| §9's deterministic counts are those of the pinned expected result | K-design (`preflight-expected.json`, `preflight_expected.py`); K-engine |
| the S16 argument is the pinned file | K-design (`S16-completeness.md`) |
| each cited design run is retained as an expected result | K-design, its row added to §9's table before `F` |
| the disclosed prior files are the pinned files | K-prior, against §13's table; `prior/` is add-only |
| `F`'s exact-head run and designation are retained by the first execution commit | K-ret-F; `retained/` is add-only |
| `E`'s exact-head run and designation reach `main` before reconciliation, and the receipt names their digests | K-ret-E |
| nothing writes to the record directory after `Q` | G13, checked by `tools/v3_verifier.py --receipts` at every later commit |
| no duration is frozen | §9: no rule reads a duration, and the expected result reads no stderr |

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

- **Before `F`:** the round's code — the run script with the `ℚ(ζ₁₆)` layer of §7, the independent replay script and
  `controls.py` — is written and its blobs are recorded here. It is exercised only in control mode, on the synthetic
  and written-answer inputs of §8, locally and on a disposable branch at the predicted tree (design evidence, not
  attestations). Each disposable-branch run this preregistration cites is retained as an expected result in
  `design/runs/` and pinned in §9's table before `F` (below). The `F` check run is dispatched with the branch held at
  exactly `F`, before the designation record is posted, and no execution commit is made before that record.
- **Stage 1, the first execution commit:** the copied objects (`objects/`, §2.1), the disclosed prior scripts and
  outputs (`prior/`, §13), the design files of §9 (`design/`), the code, each at its frozen blob, and `retained/F/`
  (below). After stage 1 every file the round cites is in its record directory or on `main`; nothing it relies on is a
  scratch file or a branch other than `main`.
- **Stage 2:** the run, twice, byte-identical; the replay; the outputs and the witness list as record files.
- **Stage 3:** the result note, its tokens printed from the outputs, with the proofs of §6.
- **`E`:** the exact-head run at `E` is dispatched before `E` is designated. Then `E`'s evidence-retention pull request
  (below), reconciliation on a base that contains it, the receipt `Q` and `tools/v3_verifier.py --verify-round Q`.

**Retention (AGENTS §A.42 items 2 and 6; proposed, §14 (h)).**

- **`F`'s exact-head run, in `retained/F/` by the first execution commit.**
  - `check-run.json`: the expected result of the run dispatched on `F`, in the form of the evidence-retention archive's
    `ci/<run>/results.json`, read from the Mathlib bridge job's log by
    `verification/audits/evidence-retention/extract_result.py` from `main`. It holds build success; the release gate's
    steps, statuses, summaries and verdict, which are the release-gate block; each governed module's `#print axioms`
    reports; and the failure markers. It names `F`, the run, the job, the recipe (`reproduce.py --run <run>`) and the
    sha256 of the served log text it was read from. Its form is derived.
  - `jobs.json`: every job of that run with its name, attempt and conclusion, read from the jobs API. Its form is
    derived.
  - `designation.json`: the owner's designation of `F`, as its text, its author and its time, with the host object it
    was posted on.
- **Disposable-branch design runs, in `design/runs/` at stage 1:** one expected result per cited run, in the form of
  `check-run.json`, naming the disposable branch's commit and tree. That commit is provenance only.
- **`E`'s exact-head run, in `retained/E/`.** No commit of the round after `E` can carry it (S9 condition 2, S10).
  - An evidence-retention commit adds `retained/E/check-run.json`, `jobs.json` and `designation.json`, in the forms
    above for `E`, and lands on `main` through its own pull request.
  - The same pull request adds to `verification/audits/evidence-retention/manifest.json` the `coverage.later` entry
    with path `verification/receipts/LOC-1.json` and evidence
    `verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/retained/`. The round cannot write
    it, because the manifest lies outside the round's governed paths.
  - Before it lands, that pull request runs `check_retention.py` plain and with `--self-test`, `--later-provenance` and
    `--gate` (§A.40).
  - The round's reconciliation takes a base that contains the evidence-retention commit (K-ret-E).
  - The receipt's candidate entry for `E` names, in its `measured` string, each file of `retained/E/` with its sha256.
  - Nothing writes to the record directory after `Q` is built. A later write fails G13 at the landing, and the round
    builds again (S10).
- **Each retained file** is scanned before it is committed for tokens, keys, signed-URL parameters, IP addresses and
  e-mail addresses (§A.42 item 5). A redaction is recorded with what was removed and where, and the redacted copy
  carries its own digest.
- **Attestations.** A retained file is evidence of an attestation, not the attestation. The receipt's `check-run` and
  `owner-designation` entries name the host objects (S5), and no retained or local output is recorded as a `check-run`
  attestation (§A.40).

**What voids the round:** a failed control of §8; a copy in `objects/` that differs from its §2.1 row (K-obj); a file in
`design/` or `prior/` that differs from its row in §9 or §13 (K-design, K-prior); a departure from P0's or P2's frozen
conventions found by K-repro; a difference between two runs; a disagreement with the independent replay.

## 13. Prior knowledge disclosed

The cells were chosen with the following knowledge. **None of these results is used as a token.** Each script and
output named below is copied into the record directory at stage 1 (`prior/`), pinned by size and sha256 in the table at
the end of this section, so that this disclosure points to content retained with the round; until then the names
identify working material, not evidence.

- **Thread B's exploratory sweep** (`prior/decomposition_probe.py` and its output), exact
  with green controls, over the 3 × 3 identifications at `CCT4` and `CCC` and the three at `CENT`: `Lcc` on `𝒪₁`
  SEP-PHYS in the three identifications that keep the declared `V`-class and SEP-REP in the other six; `We.X` SEP-PHYS
  on all three carriers in all nine; `WW.Ke` SEP-PHYS on `𝒪₂` and `𝒪₃` in all nine; `CCC`'s `Γ` a product in six of
  nine, with `Ucv` SEP-REP there; `CN` a non-product in all three. Its SEP-REP certification used hand-built product
  lifts; these rules replace it with W-REP and keep two of those lifts only as the K-rep control.
- **The four-site countermodel** (#851's check, `prior/factorization_check.py` and its output): on `S-ring(3)` the
  natural factorization has `deg_max = 3` and 8 edges and the eigenmode one `deg_max = 1` and 4 edges; the φ-pullback
  has the natural graph and is distinct. These are K-ring's numbers, which the round re-derives.
- **Thread B's closure design** (`prior/closure_design.py` and its output): on `U-free(3)` and
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

**Files copied to `prior/` at stage 1.** Each row is one file. Its copy is `prior/<file>`, byte-identical to the working
file pinned here; K-prior checks every copy against its row. Each script uses the standard library only and reads no
file. Rerun in a fresh copy on 2026-10-17, each reproduced its output byte for byte.

| file | what | form | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `decomposition_probe.py` | thread B's `explore/decomposition_probe.py` | complete-as-cited | 14708 | `acdd998dd477b3fca26e41210b0f5b1634d0e795d47df4b4c1de1aad6472d40a` |
| `decomposition_probe.out` | its output | complete-as-cited | 6381 | `f32b7f820df7b80e2980b1a6409aea6e3e06aba2a3c12fe76e132b020acc527a` |
| `factorization_check.py` | #851's check of the four-site countermodel | complete-as-cited | 5496 | `52694d4afd14c472ec9e7e265dae19183651e57cc284346d8d36981953a29126` |
| `factorization_check.out` | its output | complete-as-cited | 1095 | `9ef260e7b54d7f339da5e3a29a30f8e62f00866c4993e82576689513f898d363` |
| `closure_design.py` | thread B's `explore/closure_design.py` | complete-as-cited | 3078 | `bb33939e6da3bd9c5638e547605d4541dae19118f6b564484fa007c34b3a7ed3` |
| `closure_design.out` | its output | complete-as-cited | 812 | `88921a9967bb57581e084323a206481baf5bce18f0d7d73f9fc6d97cfb5cb1d8` |

## 14. Owner decisions

**Made on 2026-10-16:**

- **The scopes.** I0, I1 and I2 as §1 states them; for I2, requiring the same abstract dynamics up to coordinate
  conjugacy is insufficient, so the condition must have discriminating content (§3.2, SC-I2). No enumeration or sampling
  result is promoted into an unrestricted uniqueness theorem (§7.V).
- **The budget** and the mandatory controls `C21`, `CT4` and the four-site countermodel (§8, §9).
- **(a) Leg T I0:** `Γ^σ` a product, by PC on `cut_stoch` (§3.2). It keeps the broader factorization test, the
  condition under which `SL-U` applies at all; the stricter `Γ^σ = Γ`, the symmetries of the visible law, is not the
  scope. At `C21`, where `Γ ≡ 1/16`, the two coincide.
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
- **(e) Round identity:** round `LOC-1`, kind non-sealing, record directory
  `verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence/`, as the `v3-round` block declares.
  The P0 and P2 research records are cited as provenance and not edited.
- **(f) Historical objects:** P0's and P2's research commits are not on `main`, and a record may not rest on content
  outside `main` (AGENTS §A.42), so citing those commits alone does not retain the objects. Every object of theirs that
  the round reads is copied into `objects/` at stage 1, byte for byte, with its source commit, path, size, blob id and
  sha256 recorded in §2.1 and verified by K-obj; `objects/` is add-only in the `v3-governed-paths` block. Landing the
  research records on `main` is not a precondition of the round.

**Proposed, for the owner's decision.** Each takes the stricter of the options considered.

- **(g) `design/`, `prior/` and `retained/` add-only (proposed).** The `v3-governed-paths` block carries `record A`
  entries for them, as for `objects/`. K-design and K-prior require, before any cell runs, that each file's size and
  sha256 equal its pinned row in §9 or §13; a mismatch voids the round (§8, §10, §12).
- **(h) Retention (proposed).** The arrangements of §12 for `F`'s and `E`'s exact-head runs, for every cited
  disposable-branch design run and for the owner's designations of `F` and `E`, checked by K-ret-F and K-ret-E (§8).
  `E`'s evidence-retention pull request also adds the archive's `coverage.later` entry for
  `verification/receipts/LOC-1.json`, which the round cannot write.
- **(i) `D`'s standing (proposed).** `D` is cited only for the repository facts the round reads: it is an ancestor of
  `F`, and it lies on the first-parent chain of every reconciliation's first parent (K3). No CI run of `D` is cited, so
  none needs retaining. The alternative is to cite `D`'s push run as a claim, with its expected result retained under
  §A.42.
- **(j) Replay independence (proposed).** The independent replay implements its own `ℚ(ζ₁₆)` arithmetic and rebuilds
  every frozen lift and rule matrix from its closed form instead of importing P0's class from `objects/` (§8). The
  alternative, importing that class, would leave the replay sharing P0's arithmetic with the run.
- **(k) The `ℚ(ζ₁₆)` layer of S16 (proposed).** `design/S16-completeness.md` argues completeness for integer entries,
  the only entries the engine as measured accepts. For `C21`'s targets the exhaustive reading of S16 (NONE certifies
  that no class exists; termination gives an exact class) holds only through a layer meeting its conditions E1–E4.
  K-arith-16 checks that layer before any run on a target, and a failure is VOID.
