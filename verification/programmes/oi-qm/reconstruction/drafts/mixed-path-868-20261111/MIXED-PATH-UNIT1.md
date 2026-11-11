# MIXED-PATH-1 — Bell scope: mixed hidden/visible paths inside the emergent-light-cone window

**WIP / UNVERIFIED, paper-only writer draft r1; not reviewed; authorizes nothing.**

- **Accountable home:** #868. Coordination #1169. Parent draft: Bell-scope unit 1 r2 (open point O2).
- **Authorization (quoted with author and time).** #868 comment 6794392080, author `amaybaum`,
  2026-11-11T11:17:53Z, titled "Owner authorization: "mixed-path window" unit (Bell scope)":
  > **Owner answer, verbatim: "I give full authorization"**

  with the coordinator's recorded reading: "The authorization covers both stages of this unit and nothing else:
  **Stage 1** as described. **Stage 2:** a small exact computation on the native rule, run only under a written
  preregistration that fixes the following before any number is seen (§A.29, §A.21, §A.41): the decision rule; the
  controls and countercontrols; the size bounds. The preregistration gets an independent check before the run.
  **Not covered:** any merge; any F/E designation or dispatch; any manuscript change; any new physical premise; any
  other unit's gated run; the Q-C2-1 design run. A result in either direction is reported as scoped evidence for
  this construction only."
- **Done in this unit:** source reading at the pin below, hand derivations, and one probe file of exact checks on
  generic mathematical objects (integer norm arithmetic, abstract `Z_q`-linear response tables, Bell tables). **No
  OI rule was stepped, simulated or enumerated, on any lattice, at any size.** No git or GitHub write. No manuscript
  or frozen record edited. Stage 2 is specified separately in `STAGE2-PREREG.md` and has not been run.
- **Corpus pin:** `main` = `cac5d26441dd33e9348151487e4df7b547195481`, an ancestor of `origin/main` when read.
  Every `main` citation is `git show cac5d264:<path>`; `Main:N`, `SM:N`, `Substratum:N`, `GR:N` are lines of
  `papers/<name>.md` there.

**Evidence tags.** **P** paper proof on `main`; **W** research record on `main`, model-reviewed (not verification,
§A.46 item 7); **N** numerical statement on `main`; **D** draft off `main`; **A** derivation in this file,
unreviewed; **X** exact generic check in this unit's probe (supports a proof, does not replace it); **L**
literature, recalled, not read first-hand in this unit.

***

## 0. Summary of findings

1. **The window (§2).** For a generator event and a record event with lattice separation `n ∈ Z³` and `k` updates
   apart, "graph-connected and spacelike for the wave speed" is exactly `‖n‖₁ ≤ k < √3·‖n‖₂`. With `θ` the angle
   between `n` and the nearest body diagonal, `‖n‖₁ = √3·‖n‖₂·cos θ`, so the window is `1 < d/(c_w·Δt) ≤ 1/cos θ`:
   the graph cone is the octahedron circumscribed about the wave sphere. The ratio runs from `1` (body diagonals,
   empty window) to `√3` (axes). It is a pure ratio: nothing in it depends on the lattice spacing. [A; X W1–W3]
2. **A finer structure the cone lemma does not see (§1.2, §2.2).** For every centre-free second-order
   nearest-neighbour rule on a bipartite lattice, the dynamics splits exactly into two non-interacting space-time
   parity classes (Lemma P). Pointwise dependence of a record on a setting therefore needs `k ≡ ‖n‖₁ (mod 2)` for a
   current-slice setting and `k ≡ ‖n‖₁+1` for a retarded-slice setting. [A]
3. **Whether hidden sites are essential depends on the partition (§1.3, §2.3).** The corpus gives four
   visible/hidden partitions. Under the 3D checkerboard and under the region (laboratory) partition every path
   between distinct visible sites passes through hidden sites: "mixed" is essential. Under the 4D checkerboard the
   hidden class is dynamically decoupled (Lemma P): there are no mixed paths at all, and any dependence is
   visible-to-visible. Under the companion partition (current field visible, retarded register hidden)
   visible-only paths exist. The Bell theorem of Main §3.3 uses regions, not the checkerboard. [A on P]
4. **Masking (§4).** Under the uniform hidden prior, no-signalling at a wing is equivalent to the remote setting
   acting on that wing's complete history as a relabelling of hidden states (PAD). [A; X P1] Two general results
   then restrict the route:
   - **Lemma S (slice shift).** For every centre-free rule of the second-order form `x(t+1) = F(x(t)) − x(t−1)`,
     linear or not, if the retarded slice at the neighbours of a generator site is uniform and hidden, a current-slice
     setting has no effect on any record *law* until two ticks after the graph cone arrives, and the two-wing
     table over windows `k ≤ ‖n‖₁+1` is Bell-local. [A]
   - **Theorem L (affine pad locality).** For an affine rule over `Z_q` — the exact linear reference rule — with a
     coset-uniform hidden prior and settings entering as generator content, complete-history no-signalling at
     both wings implies that the complete-history table is Bell-local. Masked dependence and Bell violation
     cannot coexist; unmasked dependence is signalling. [A; X L1–L3]
   - The coset hypothesis cannot be dropped: an additive setting dependence with a non-affine conditioning event
     gives a no-signalling table with CHSH `3` (generic `Z₄` example, fitted, not native). [X X1]
5. **Consequence for the route.** On the exact linear rule with the uniform prior (or any prior obtained by
   conditioning on exact record values, which are affine events), the O2 window cannot supply a Bell violation.
   What stays open is the non-linear branch (the rounded rule of SM §4.2) and non-affine preparations; for the
   former, the first open instances are a retarded-slice setting at `k = ‖n‖₁+1` (axis `(D,k) = (2,3)`) and a
   current-slice setting at `k = ‖n‖₁+2` (axis `(3,5)`, or `(4,6)` with both wings on even sites). Stage 2 is
   aimed there, with the linear rule as a proof-backed control.
6. **Empirical confrontation (§5).** If the mechanism worked, every-run Bell violation would require the timing
   margin `m = d/(cΔt)` to satisfy `m ≤ 1/cos θ ≤ √3`: no violation at any orientation for `m > √3`, and for
   smaller margins none while the wing axis is within `arccos(1/m)` of a lattice body diagonal. The cut-off is
   scale-free and is not washed out by the size of the laboratory. Quantum mechanics has no such cut-off. Bell
   violations at margins far above `√3` are on record with coincidence post-selection [L]; a loophole-free
   violation at `m > √3` would be a direct miss. The favourable reading needs nature to violate Bell inequalities
   only at small margins and every large-margin violation to be a detection artefact. That is a severe cost.
7. **§A.29 (§6).** "`c` = wave speed + mixed-path dependence" is not adopted. It is falsifiable in shape, but it
   has no derived mechanism, Theorem L removes it on the linear rule, and its distinctive prediction is
   disfavoured by existing data read at face value.

***

## 1. Definitions from the corpus

### 1.1 Sites, state, and the update rule

- **Sites and state.** Site factorization is ledger posit (viii): "the configuration space is identified with a
  product of local configuration spaces over a set of sites" (Main:726) [P, posited]. The second-order form is
  ledger posit (xiii), "a posit of the selected lattice model, not derived and not an axiom of OI: each site of
  (viii) carries a previous and a current value in a finite abelian group, and one step is
  `x(t+1) = F(x(t)) − x(t−1)`, in phase-space form `(x(t−1), x(t)) ↦ (x(t), F(x(t)) − x(t−1))`" (Main:726). Write
  `u = x(t)`, `v = x(t−1)`; the site component is `S_i = {(u_i, v_i)}`.
- **Lattice.** `d = 3` simple cubic, a selected input ("the cubic lattice is not itself derived", SM:14); the
  nearest-neighbour range is ledger posit (x) (Main:726).
- **Rules on record.** The corpus does not name one finite map as *the* realized one: "Whether one realized map
  supports both the structural chain and the required stationary law remains open" (SM:298). It records:

  | Label | Rule | Source | Status in the corpus |
  |---|---|---|---|
  | **R-lin** | `u' = A u − v (mod q)`, `A` the six-neighbour sum, coefficient 1 | `papers/oi_lattice_code/trace_out_fractional/wave_eqn.c`:6–10; SM:298 ("The exact finite update `f = Σ_nn x − x(t−1)` over `Z/qZ` is modular-linear"); Main:726 (instance `q = 2`); used at `q = 2`, `L ≥ 9` by `correlation-recombination-20261107/DESIGN.md` §1 and `NO-SIGNALLING.md` §3 [W] | the reference finite update; linear (ledger (vii)); integrable, not ergodic on its shells (SM:294–296) |
  | **R-norm** | `u' = α A u − v (mod q)`, `α = 1/d` | SM:296 ("at `α = 1/d` (when `d` is invertible modulo `q`)"); SM:232 | exists only for `3 ∤ q`; at `q = 2` it equals R-lin |
  | **R-round** | `u' = ⌊(Σ_nn u + 1)/3⌋ − v (mod q)` on representatives `0..q−1` | SM:294; code convention `papers/main_repro/lyapunov_v3.py`:18–19 (`np.roll(±1)` neighbour sum) | the non-linear candidate for "way out (i)"; chaos indicated numerically [N] |
  | R-ring | state-dependent neighbour on a ring, `d = 1` | SM:112 | explicit state-dependent-graph example; no emergent speed is derived for it; outside this unit |
  | observer-level lift | `φ(n,t+1) = (1/d)Σ_j[φ(n±ê_j,t)] − φ(n,t−1)` over the reals | SM:278–282 (Theorem 1) | conditional on Corollary 1b (observer-level centre-freeness); "the map `φ → L_obs → Δ_g` is not proved anywhere in this framework" (SM:232) |

  The header of `wave_eqn.c` says "alpha=1 fixed by max-signal-speed"; SM:240 withdraws that selector, and
  `NO-SIGNALLING.md` §6 already cites the file for its step equations only.

### 1.2 Stencil, coupling graph, graph cone

- **Coupling graph.** `i ∼ j` "whenever the `i`th output component of `φ` depends on the `j`th input component for
  some state (symmetrized for the spatial graph)" (Main:364; same definition SM:66). For R-lin, R-norm and R-round,
  site `i`'s output `(u_i', v_i') = (F_i(u|_{N(i)}) − v_i, u_i)` reads its six neighbours and itself, so `G_φ` is the
  simple-cubic graph with a self-loop at each site. [A, immediate]
- **Cone lemma.** "`(φ^k(s))_i` depends only on initial components in the graph ball `B_{G_φ}(i,k)`" (Main:364)
  [P]. The hop metric of the simple-cubic graph is the `ℓ₁` metric (SM:150: "`a·d_G(x,y) = ‖x−y‖₁` at every
  spacing `a`") [P].
- **Lemma P (space-time parity classes) [A].** *Let the site graph be bipartite with colouring `ε(i) ∈ {0,1}`, and
  let the rule be `x_i(t+1) = F_i(x_j(t) : j ∼ i) − x_i(t−1)` with `F_i` not reading `x_i(t)` (centre
  independence, ledger (xi), second clause). Put `C_p = {(i,t) : ε(i)+t ≡ p (mod 2)}`. Then the values on `C_p` at
  all later times are functions of the values on `C_p` at times `t_s`, `t_s−1` alone: the phase space is a product
  `S^E × S^O` and the map is a product of two maps.* *Proof.* If `(i,t+1) ∈ C_p` then `(j,t) ∈ C_p` for `j ∼ i`
  and `(i,t−1) ∈ C_p`; induct on `t`. ∎ At the slice `t_s`, class `E` (containing `(even, t_s)`) holds `u|_even` and
  `v|_odd`; class `O` holds `u|_odd` and `v|_even`. On a torus the lemma needs every side even. It holds for
  R-lin, R-norm and R-round; it fails for R-ring, whose selector reads a same-parity site. The corpus states the
  ingredient ("even sites couple only to odd sites and vice versa", SM:539) and observes the consequence
  numerically (a perturbation "saturates the perturbed parity sublattice", SM:294 [N]); a corpus search for
  `space-time parity`, `4D parity`, `two decoupled`, `parity sector` found no statement of the decoupling itself.
  The cone lemma is therefore not sharp: Main's sites carry both classes, and `G_φ` joins them through the
  self-loop only as bookkeeping.

### 1.3 Visible and hidden: four partitions in the corpus

| Label | Visible / hidden | Source | Role in the corpus |
|---|---|---|---|
| **Π_gen** | an abstract product `C_V × C_H`; the visible law from a visible root `a` is `Γ_t(a,j) = μ_H{h : π_V φ^t(a,h) = j}` | Main:115, Main:137, Main:143; uniform `μ_H` is the default ("under the uniform hidden prior that defines `T`", Main:131) | the definition every emergence theorem uses; it fixes what "record law under the hidden prior" means: visible root fixed, hidden drawn from `μ_H` |
| **Π_hor / Π_reg** | a spatial region and its complement: "degrees of freedom beyond causal reach are permanently hidden" (Main:28); "a candidate partition — a cosmological horizon, a laboratory apparatus, an equilibrium fluctuation" (Main:72); "The physical partition (the cosmological horizon) traces out a spatial region containing both sublattices" (SM:539) | Main, SM | the physical realization. With a horizon partition, both wings and everything between them are visible |
| **Π_cb** | checkerboard: "site **n** [is in] the visible sector iff `(−1)^{Σ n_μ} = +1` (even sublattice)" (SM:537); in Theorem 13 the grading is the 4D parity `ε_4D`, "equivalent to the 3D spatial sublattice grading … for static observables" (SM:557) | SM §4.7–4.8 (Theorem 12: "The OI checkerboard partition coincides with the staggered ε-grading") | the matter-sector trace-out. Two site-level readings: **Π_cb3** (even spatial sites, both slices) and **Π_cb4** (one space-time parity class) |
| **Π_comp** | "current field visible, retarded register hidden" (SM:252, Lemma 1c(iii)); "the visible sector one site's two time slices" (SM:112) | SM §4.1, §3.1 | the companion realization behind the dispersion relation |

A fifth usage is not a site partition: the "timescale-selected momentum region" (SM:136) and "the infrared
effective theory obtained by integrating out modes near the lattice scale" (SM:549).

**Which the Bell setup uses.** Main's theorem (Main:366–393) and Corollary (Main:416) are stated with wing regions
`A`, `B`, readout regions `R_A`, `R_B` and a pre-setting variable `Ω`; neither mentions the checkerboard. Bell-scope's
class 𝒞_sep [D] likewise uses generator and record regions and `Ω = x_{t_s}|_W`. That is a region-type partition
(Π_reg): the wings' records are visible and everything else is carried by `Ω`. The owner's phrase "the interleaved
hidden and visible sites" corresponds to Π_cb3.

**Finding C-1 (corpus ambiguity; reported, not corrected).** SM:539 calls the checkerboard "the OI partition
(visible vs. hidden)" and, in the same remark, says the physical partition is the horizon, containing both
sublattices. The corpus does not say which partition supplies the hidden prior for a laboratory Bell protocol.
Every partition-dependent statement below is made per partition, and Stage 2 enumerates them.

### 1.4 The emergent wave speed and its status

| Quantity | Value | Status |
|---|---|---|
| graph-cone speed in direction `n̂` | `1/‖n̂‖₁` spacings per update, from `1` (axes) to `1/√3` (body diagonals) | proved from the cone lemma and the `ℓ₁` metric (Main:416; SM:150) [P] |
| long-wavelength wave speed `c_w` | `1/√d = 1/√3` in every direction; `cos ω = (1/d)Σ_j cos(k_j a)` | derived for the observer-level lift (SM:230, SM:282), which is conditional on Corollary 1b and on the unproved bridge `φ → L_obs` (SM:232). Isotropy of the quadratic symbol: SM:258–266 [P, kernel-checked] |
| the physical `c` | not identified | "which of the two, if either, is the physical `c` … is not derived here" (Main:416); likewise SM:230, Substratum:131 |
| one emergent light cone for all matter | assumed where used | conditional: "if its single-cone structure holds" (GR:166), resting on loop-level `O_h` invariance and an `O`-equivariant condensate under H-link |

This unit takes "`c` = `c_w`" as the hypothesis under examination. It is option O2-C of the decision sheet: a new
identification, not a result.

***

## 2. The window, exactly

### 2.1 Definition and characterization [A; X W1–W3]

A *generator event* is (site `g`, tick `t_s`); a *record event* is (site `r`, tick `t_s+k`); `n = r − g ∈ Z³`.

- graph-connected: `‖n‖₁ ≤ k` (cone lemma; otherwise no dependence, exactly);
- spacelike for the wave speed: `‖n‖₂ > c_w·k`, that is `k² < 3·(n·n)`.

**Window.** `𝒲 = {(n,k) : ‖n‖₁ ≤ k and k² < 3 n·n}`. For a given `n` the admissible ticks are the integers in
`[‖n‖₁, √3‖n‖₂)`.

**Geometry.** For `n` in the positive octant, `‖n‖₁ = n·(1,1,1)`, and in general `‖n‖₁ = max_s |n·s|` over the
sign vectors `s ∈ {±1}³` (X W2). Hence `‖n‖₁ = √3·‖n‖₂·cos θ`, `θ` the angle from `n` to the nearest body diagonal,
and

`(n,k) ∈ 𝒲  ⟺  1 < ‖n‖₂/(c_w k) ≤ 1/cos θ.`

The graph cone at tick `k` is the octahedron `‖x‖₁ ≤ k`; the wave sphere `‖x‖₂ = k/√3` is its inscribed sphere,
touching it at the eight face centres, which lie on the body diagonals. The window is the octahedron minus the
closed ball.

| Direction | `cos θ` | cone/wave ratio `1/cos θ` | window ticks for small `n` |
|---|---|---|---|
| axis `(D,0,0)` | `1/√3` | `√3 ≈ 1.732` | `D=1`: {1}; `D=2`: {2,3}; `D=3`: {3,4,5}; `D=4`: {4,5,6}; `D=5`: {5,…,8} |
| face diagonal `(D,D,0)` | `√(2/3)` | `√(3/2) ≈ 1.225` | `D=2`: {4}; `D=4`: {8,9} |
| body diagonal `(D,D,D)` | `1` | `1` | empty for every `D` (equality case of Cauchy–Schwarz) |

The window is empty only on the four body-diagonal axes, a set of directions of measure zero. Near a body diagonal
it is thin: the relative width is `1/cos θ − 1 ≈ θ²/2`. The set of directions whose ratio is at least `m` is the
complement of eight caps of half-angle `arccos(1/m)`; for `m ≤ √(3/2)` the caps are disjoint and cover the
fraction `4(1 − 1/m)` of the sphere; for `m → √3` only the axes remain.

**Scale.** `𝒲` is defined by a ratio. Rescaling `n` and `k` together maps `𝒲` to itself up to the integer
rounding of `k`, and "A clock and length calibration rescales both speeds by the same factor" (Main:416). The
`ℓ₁` stretch "does not decay, in flat space, in the continuum limit or anywhere else" (SM:150). The window is
therefore the same fraction of the light-cone exterior at laboratory scale as at lattice scale.

### 2.2 Which paths realize it, and the parity refinement [A]

Write the dependency relation of the second-order rule on space-time: `(i,t+1)` reads `(j,t)` for `j ∼ i` and
`(i,t−1)`. A dependency path from `(g,t_s)` to `(r,t_s+k)` consists of `m` spatial hops and `ρ` retarded steps
with `m + 2ρ = k`, `m ≥ ‖n‖₁`, `m ≡ ‖n‖₁ (mod 2)`.

- **Cone boundary** (`k = ‖n‖₁`): only shortest lattice paths, `ρ = 0`; there are `k!/(|n_x|!|n_y|!|n_z|!)` of them.
- **Parity.** By Lemma P a current-slice value `u(g)` can influence `u_k(r)` only if `k ≡ ‖n‖₁ (mod 2)`; a
  retarded-slice value `v(g)` only if `k ≡ ‖n‖₁+1 (mod 2)` and `k ≥ ‖n‖₁+1`. So half the ticks of `𝒲` are excluded
  for each kind of setting, and `𝒲` splits into `𝒲_u` and `𝒲_v`.
- **R-lin, pointwise dependence at the boundary.** `u_k = S_k(A)u_0 − S_{k−1}(A)v_0` with `S_0 = 1`, `S_1 = A`,
  `S_{k+1} = A S_k − S_{k−1}`. The coefficient of `u_0(g)` in `u_k(r)` at `k = ‖n‖₁` is the path count above; on an
  axis it is `1`, a unit in every `Z_q`. So on R-lin a setting at `g` changes the record `u_D(g+Dê_x)` for every
  configuration and every `q`: a dependent pair exists inside the window (all axis `D ≥ 1`). For other directions
  the coefficient is a multinomial and can vanish modulo `q` (for `q = 2`, whenever the base-2 addition of the
  `|n_j|` carries). For R-norm the same count is multiplied by the unit `α^k`. For R-round nothing is asserted
  here: SM:294 reports that a perturbation "spreads at about one site per step in lattice distance" after the
  first alphabet-boundary crossing [N, at `L = 20`, `q = 2^16`], which is evidence that its dependence fills the
  graph cone, not a proof.

### 2.3 Is "mixed" essential? Per partition [A]

A *mixed* path is one with at least one interior event at a hidden site (or in a hidden class).

| Partition | Paths between distinct visible sites inside `𝒲` | What changes |
|---|---|---|
| **Π_cb3** (even sites visible) | every spatial hop changes sublattice, so every path of length ≥ 2 has interior hidden sites; **no visible-only path exists** | wings must sit on even sites, so `‖n‖₁` is even. In class `E` the setting is `u|_even` and the hidden data are `v|_odd`; in class `O` the setting is `v|_even` and the hidden data are `u|_odd` |
| **Π_reg** (wing sites visible) | every path leaves the wing, so **mixed is essential** for non-adjacent wings | all of `Ω` is hidden; this is Bell-scope's setting |
| **Π_cb4** (one space-time class visible) | by Lemma P the hidden class never influences the visible one: **there are no mixed paths**; every dependency path is visible-only | no hidden coordinate lies in any record's dependency set, so record laws are point masses and any dependence is deterministic visible-to-visible propagation at the graph speed |
| **Π_comp** (current field visible) | a path of spatial hops only uses current-slice events: **visible-only paths exist**, and they are the shortest ones | the hidden retarded register enters each update once, additively |
| **Π_hor** (horizon) | both wings and all intermediate sites are visible: no hidden site in the patch | as Π_cb4: nothing to average over |

So the phrase "mixed hidden/visible paths" describes Π_cb3 and Π_reg. Under Π_cb4 and Π_hor the same graph
connectivity exists with no hidden site on it, and "`c` = wave speed" would then mean that the visible sector's own
exact dynamics carries dependence faster than `c`.

### 2.4 Anisotropy: `ℓ₁` against `ℓ₂`

SM:150 states that "the substratum has two distinct emergent geometries — a propagation/spectral geometry that is
`ℓ₂`, and an intrinsic shortest-path geometry that is `ℓ₁`". The window is the gap between them. Its size per
direction is `1/cos θ − 1` in units of the light-cone radius. One qualification from the corpus: SM:108
constraint (iii) asks that a state-dependent graph `G(x)` be "statistically isotropic on large scales for typical
reference configurations". On the fixed simple-cubic reference graph the anisotropy is exact at every scale. On a
state-dependent graph satisfying (iii) the graph cone could be isotropic, and the window would then be a
direction-independent ratio that the corpus does not compute.

***

## 3. Bell mapping

**Which hypothesis of Theorem N fails.** For a protocol whose generator-to-remote-record pairs lie in `𝒲`, (Sep)
fails: `d_{G_φ}(G_B, R_A^t) ≤ t − t_s` for some `t` in the record window. Nothing else in 𝒞_sep is affected.

**What that implies.** Only that Theorem N and Main's Corollary do not apply ("Wings separated by less than the
graph cone over the experiment's duration fall outside the Corollary", Main:416).

**What it does not imply.**
1. *Not a dependence.* (Sep) is sufficient for parameter independence, not necessary. A graph path is an upper
   bound on the dependency set. The parity refinement (§2.2) and vanishing coefficients modulo `q` remove
   dependence on part of `𝒲`.
2. *Not a law-level dependence.* A pointwise dependence can be exactly masked by the hidden prior (§4); then the
   record law is setting-independent.
3. *Not a Bell violation.* Masked dependence may still be Bell-local: by Lemma S it is, for windows
   `k ≤ ‖n‖₁+1`; by Theorem L it always is on an affine rule with a coset-uniform prior.
4. *Not an escape for OI.* A violation on a finite instance would be a construction-scoped finding.

**What would be needed.** Keeping measurement independence and every-run outputs, a Bell violation needs all of:

- (D1) a *directed* dependence generator → remote record inside the record window: for some pre-setting state,
  `h_A(λ, a, b) ≠ h_A(λ, a, b')`. This is a failure of **parameter independence** (Main's option (a), Main:414);
  outcome independence is automatic under determinism. A path through a shared hidden site that no setting writes
  is a common cause and does not count (SUBSTATE-BRIDGE-1 lemma L3 [D]);
- (D2) on both wings, or on one wing with the other wing's response correlated through `Ω`: a one-way dependence
  can already violate CHSH;
- (D3) masking: complete-history no-signalling (§4), property N3 of SUBSTATE-BRIDGE-1;
- (D4) *non-factorizable* masking: the relabellings of hidden states that mask the two wings must not combine
  into one setting-independent variable (§4.2). On an affine rule they always combine;
- (D5) a bound: the mechanism should give CHSH in `(2, 2√2]` (property N4); a channel with a fair pad gives the
  PR value (Main:362; composition-source-map §5.2 [W]).

In the window, the mixed-path route supplies a candidate for (D1) natively: no long edge, no non-site-fibred
factor (N1), no prepared pair. It supplies (D3) only where §4 shows it, and nothing in this unit supplies (D4) or
(D5).

***

## 4. No-signalling: the masking condition

### 4.1 General form [W, then A]

Fix the response-complete pre-setting variable `λ` with law `μ`, and the complete local histories `h_A(λ,a,b)`,
`h_B(λ,a,b)`.

- **(M1) Balance.** B's complete history law is independent of A's setting exactly when
  `Σ_λ μ(λ)·(1[h_B(λ,a,b) = h] − 1[h_B(λ,a',b) = h]) = 0` for every `h`, `b`, `a`, `a'`
  (prepared-pair-source §4, Balance lemma [W]). Equality of one-read marginals is not enough
  (`NO-SIGNALLING.md` §1 item 2 [W]).
- **(M2) Under the uniform prior, masking is a relabelling [A; X P1].** If `μ` is uniform on a finite set `Λ`,
  (M1) holds iff for every `b`, `a`, `a'` there is a bijection `σ` of `Λ` with
  `h_B(σλ, a', b) = h_B(λ, a, b)`: equal counts of each history are the same thing as a bijection matching them.
  This is condition (PAD) of SUBSTATE-BRIDGE-1 §3.4 [D], which is there sufficient; under the uniform measure it
  is also necessary.
- **(M3) Over a family of preparations.** If (M1) holds for every law in a family whose affine span is the whole
  simplex over `Λ`, each history is pointwise independent of the remote setting (prepared-pair-source §5 [W]) and
  CHSH ≤ 2. So masking is a property of a *restricted* prior class. For the uniform prior the restriction is: the
  pad coordinates are hidden and unconditioned.

### 4.2 From masking to Bell locality: joint relabelling [A]

**Joint PAD.** Suppose there are `μ`-preserving bijections `τ_{ab}` of `Λ` and functions `f_A`, `f_B` with
`h_A(τ_{ab}λ, a, b) = f_A(λ, a)` and `h_B(τ_{ab}λ, a, b) = f_B(λ, b)`. Then
`P(h_A,h_B | a,b) = Σ_λ μ(λ)·1[h_A = f_A(λ,a)]·1[h_B = f_B(λ,b)]`: the table is Bell-local. PAD at each wing
separately is no-signalling; joint PAD is locality; the PR table has the first and not the second. A Bell
violation with no-signalling lives exactly in the gap.

**Lemma S (slice shift) [A].** *Let the rule have the form `u' = F(u) − v` of ledger (xiii), with `F`
centre-free (`F_j` does not read `u(j)`; ledger (xi), second clause) and otherwise arbitrary. Let
`P` be a set of sites such that, at `t_s`, `v|_P` is uniform and independent of all other coordinates. Let the
settings be current-slice values `a = u(g_A)`, `b = u(g_B)` with every neighbour of `g_A` and of `g_B` in `P`.
Then (i) for each wing the law of the records at a site `r` at ticks `t ≤ d(g,r)+1` does not depend on the remote
setting, `g` the remote generator; (ii) if both record windows end by `d+1`, the complete-history table is
Bell-local.*

*Proof.* For fixed `u`, the map `v|_P ↦ u_1|_P = F(u)|_P − v|_P` is a bijection, so `u_1|_P` is uniform and
independent of `u` and of `v` off `P`. Describe the run by `(u_0, u_1|_P, v|_{off P})`. Off `P`,
`u_1(j) = F_j(u_0) − v(j)` does not read `u_0(g)`: `F_g` does not read `u_0(g)` (centre-freeness), and every
other site whose `F_j` reads `u_0(g)` is a neighbour of `g`, hence in `P`. From tick 2 on,
`u_{t+1} = F(u_t) − u_{t−1}`, and `u_0(g)` enters only through `u_2(g) = F_g(u_1) − u_0(g)`. Its influence then
advances one edge per tick and reaches `r` no earlier than tick `2 + d(g,r)`. So with
`λ' = (u_0 off the generators, u_1|_P, v|_{off P})`, whose law is the same for every `(a,b)`, each wing's records
up to tick `d+1` are functions of `(λ', own setting)`. ∎

The hypothesis holds under Π_comp (`P` = all sites), under Π_cb3 for settings on even sites (`P` ⊇ odd sites), and
under Π_reg for single-site wings. Consequences: the pointwise cone and the *law-level* cone differ by two ticks
for a current-slice setting, so the law-level window is `‖n‖₁+2 ≤ k < √3‖n‖₂`, which on an axis is empty for
`D ≤ 2` and first non-empty at `(D,k) = (3,5)`; under Π_cb3, where both wings sit on even sites and `D` is even,
at `(4,6)`. A retarded-slice setting
`v(g)` has no such pad: it enters `u_1(g) = F_g(u_0) − v(g)` directly, and law-level dependence is possible from
`k = ‖n‖₁+1`, first at `(D,k) = (2,3)`.

**Theorem L (affine pad locality) [A; X L1–L3].** *Let the state space be a finite abelian group and the rule
affine (R-lin, R-norm; ledger (vii)). At `t_s` let the non-generator coordinates `Ω` be uniform on a coset
`ω₀ + K`, and let setting value `a` (resp. `b`) select generator content uniform on a coset `c_a + K_A`
(resp. `c_b + K_B`), the three independent. Write the complete histories as
`h_A = M_A κ + V_A c_a + V'_A c_b + const`, `h_B = M_B κ + W_B c_a + W'_B c_b + const`, with
`κ ∈ K̃ = K × K_A × K_B` uniform. Then:*
1. *(masking criterion) B's history law is independent of `a` iff `W_B(c_a − c_{a'}) ∈ M_B K̃` for all `a, a'`;
   symmetrically for A;*
2. *(locality) if both wings are no-signalling, the complete-history table is Bell-local with a uniform,
   setting-independent hidden variable; hence CHSH ≤ 2 for every pair of outcome maps;*
3. *(trichotomy) every such protocol is in exactly one of: no pointwise remote dependence; dependence, masked,
   Bell-local; signalling. "Bell violation with no-signalling" does not occur.*

*Proof.* (1) `M_B κ` is uniform on the subgroup `M_B K̃`, so the law of `h_B` is uniform on the coset
`W_B c_a + W'_B c_b + M_B K̃`; two such laws agree iff the cosets agree. (2) Choose `δ_a, δ'_b ∈ K̃` with
`M_B δ_a = W_B(c_a − c_0)` and `M_A δ'_b = V'_A(c_b − c_0)`, and put `κ' = κ + δ_a + δ'_b`, uniform on `K̃` for
every `(a,b)`. Then `h_A = M_A κ' − M_A δ_a + V_A c_a + V'_A c_0` is a function of `(κ', a)` and
`h_B = M_B κ' − M_B δ'_b + W_B c_0 + W'_B c_b` is a function of `(κ', b)`. (3) follows. ∎ The probe checks (1) in
both directions and the explicit local model of (2) on 400 random `Z_q`-linear response models, `q ∈ {2,3,4}`
(X L1–L3: 54 signalling cases, 309 cases of masked pointwise dependence, all local).

*Scope of Theorem L.* It needs (a) an affine rule; (b) a prior that is uniform on a coset and a product across
generators and the rest (Bell-scope's (CF) with affine events); (c) settings whose fibres are cosets with a common
direction. Conditioning on exact values of earlier records keeps (b)'s coset form, because on an affine rule every
record is an affine function of the state. Conditioning on a non-affine event does not: with `Z₄` pads `p_A, p_B`
conditioned on `p_B = σ(p_A)` for the non-affine permutation `σ = (0 1)`, and histories `p_A + b`, `p_B + a`, the
table is no-signalling, admits a single support-compatible deterministic strategy, and reaches CHSH `3` under a
binary coarse-graining (X X1; with `σ = id` it is local, X X1d). That example is fitted and has no native source;
it shows the hypothesis is needed, nothing more. A prior that correlates generator content with `Ω` is outside
the theorem; it is a measurement-independence question (O3).

### 4.3 Can the uniform counting measure supply masking?

- **For one tick, always.** The update subtracts the retarded value, so wherever the retarded slice is hidden and
  uniform it is a one-time pad on the next current value (Lemma S). This is the mechanism by which the visible
  one-step law is not a permutation (SM:112).
- **For the affine rules, by a rank condition.** Theorem L(1): masking holds iff the remote setting's column in
  the wing's history lies in the image of the hidden directions. For a single-site record at `r` and a
  current-slice setting at `g`, the reflected site `2r − g` has the same column by the reflection symmetry of
  `A`, so masking holds whenever that site's coordinate is hidden and unconditioned. It can fail when the pad
  coordinates are visible (pinned) or for multi-site record regions; that is a computation.
- **For R-round, unknown beyond Lemma S.** A retarded-slice setting under Π_cb3 enters `u_1(g) = F_g(hidden) − a`
  with no pad between the setting and its first use, and `F` is not additive. Whether the record law at
  `k = ‖n‖₁+1` then depends on the setting is not decided by any argument here.

**What would have to be shown** for masking to be a property of OI and not of one prior:
1. (S1) the pad coordinates are hidden under the partition that actually governs a laboratory (finding C-1);
2. (S2) they stay uniform given everything the wing can have recorded earlier. In a reversible world earlier
   records are functions of the same state. For a single site the pad coordinates on the shell at distance `k`
   number of order `k²` against one record per tick, so a counting argument makes exhaustion implausible; no
   proof is given;
3. (S3) masking holds for complete histories and continuations, not for one read (reuse; prepared-pair-source §4);
4. (S4) the Lemma 3 measure is the operative one. A structured preparation is permitted by Main:60, and a
   non-uniform pad signals (the non-equilibrium signalling familiar from de Broglie–Bohm theory [L]).

***

## 5. Empirical confrontation (§A.24)

**Classification of the data.** Whether a Bell inequality is violated in a given run geometry is a raw-direct
observable: counts in settings-labelled bins, with measured distances and timings. It passes through no
model-dependent pipeline. A miss here is a miss.

**The prediction, if the route worked.** Let `d` be the wing separation and `Δt` the time from the remote setting
being fixed to the end of the local record window, in the lattice rest frame, and `m = d/(cΔt)` the spacelike
margin (`m > 1` closes the locality loophole). With `c = c_w`, measurement independence and every-run outputs:

- (E1) **margin cut-off.** A violation requires a generator-to-record pair in `𝒲`, so `m ≤ 1/cos θ ≤ √3`. For
  `m > √3 ≈ 1.732` Theorem N applies at every orientation and CHSH ≤ 2;
- (E2) **orientation dependence.** For `1 < m ≤ √3` a violation is possible only while the wing axis is farther
  than `arccos(1/m)` from every lattice body diagonal. For `m = 1.05` the excluded caps have half-angle `17.8°`
  and cover `19%` of directions; for `m = √(3/2)`, `73%`. A laboratory axis sweeps a cone once per sidereal day,
  so the violation would switch off and on with sidereal phase, fully, not as a small modulation;
- (E3) **body diagonals.** Along a body diagonal there is no window at any margin.

**Is it observable or washed out?** It is not washed out by scale. The cut-off is a ratio of two speeds that a
common calibration cannot equalize (Main:416), and the `ℓ₁` stretch does not decay with distance (SM:150). The
lattice spacing does not enter. Three things could blur it, none of which the corpus establishes: (i) a
state-dependent graph that is statistically isotropic (SM:108 (iii)) would replace (E2)–(E3) by a
direction-independent cut-off and leave (E1) with a different constant; (ii) the laboratory's velocity relative to
the lattice frame changes margins at order `v/c ~ 10⁻³`; (iii) domains with different lattice orientations are not
part of the framework. What is not scale-free is the *size* of the dependence: on the real lift the response
outside the wave cone is exponentially small in `k`, while on the exact modular rule a dependence is all-or-nothing
modulo `q`. The route needs the exact discrete dependence, not the observer-level wave, to steer a macroscopic
outcome across `~10³⁵` sites.

**Raw-direct facts [L, recalled; no source read first-hand in this unit].**
- Bell violations are observed for many laboratory orientations and continuously over days; no sidereal on/off
  pattern in a Bell test is known to this writer. No search was made.
- Loophole-free tests (2015 onward: electron spins over 1.3 km, photons over tens to hundreds of metres, atoms
  over 400 m, superconducting circuits over 30 m) close the locality loophole with modest margins. Their exact
  margins `m`, as defined above, were not extracted.
- Earlier locality-loophole tests with fast random switching report margins far above `√3` (for example a
  separation of 400 m against a measurement time under 100 ns, `m` of order 10), with coincidence post-selection
  (fair sampling), and full-strength violation.

**What would count as a miss.**
- (X1) One every-run (detection-loophole-free) violation with `m > √3`, at any orientation: refutes (E1) on the
  fixed cubic reference graph.
- (X2) An every-run violation that persists at a sidereal phase where the wing axis is inside an excluded cap:
  refutes (E2). Since the lattice orientation is unknown, the test is the absence of any dead interval of the
  predicted duty cycle `≈ 4(1 − 1/m)` across a sidereal day in a continuously running loophole-free test.
- (X3) An every-run violation with a body-diagonal wing axis, once an orientation is fixed by (X2)-type data.

**Skeptical reading of the favourable case.** The route survives the recalled data only by two escapes: the
loophole-free tests happen to have small margins, and every large-margin violation is assigned to the detection
loophole. The second requires that fair sampling fails precisely where the margin is large and holds well enough
that the loophole-free and the post-selected experiments agree with the same quantum prediction. Quantum mechanics
predicts no dependence on `m` or on orientation and is confirmed in both regimes. A mechanism under which the
violation is real at `m < √3` and an artefact at `m > √3`, with the same observed value, is not credible without
independent evidence. On the recalled data the route is disfavoured, short of formally excluded; a first-hand
margin table for the loophole-free tests would settle (X1), and if any of them has `m > √3` the route is excluded
for the fixed cubic graph. That check is not done here (§8).

Consistency note: `book/ch04-methodology.md`:128 states that "the dispersion is subluminal everywhere on the
momentum sphere; superluminal LIV anywhere falsifies". That sentence concerns the dispersion relation, not
pointwise dependence, but a mechanism that uses dependence at up to `√3·c` sits uneasily beside it, and unmasked
it would be controllable signalling faster than `c` in the lattice frame.

***

## 6. §A.29 disposition: "`c_phys` = wave speed + mixed-path dependence" (not adopted)

| Requirement | Assessment |
|---|---|
| **Existing results it must preserve (its controls)** | the cone lemma and Main's ceiling outside the graph cone (unchanged); the isotropic quadratic dispersion and `c_w = 1/√3` (it adopts them); operational no-signalling for every admitted preparation (not shown beyond §4); the area-law and gauge constructions on the reference graph (untouched, since no edge is added); measurement independence (kept as a posit); H-Bell (iii), curvature stability (trivially kept: no prepared edge). It does **not** preserve the corpus's use of "superluminal … falsifies" as a falsifier unless masking is exact |
| **Independent prediction beyond the problem it fixes** | yes, and sharp: (E1) the margin cut-off `m ≤ √3`, (E2) full sidereal switching with duty cycle `4(1 − 1/m)`, (E3) no violation along body diagonals; plus signalling for non-uniform pads. None is a retrodiction |
| **Adjustability** | on the fixed simple-cubic graph: none; the cut-off is a pure number. Two escape hatches exist and would have to be closed in advance: a statistically isotropic `G(x)` (changes the constant and removes orientation dependence) and reassigning large-margin violations to the detection loophole. With either left open the proposal can be fitted to any outcome and fails §A.29 |
| **Mechanism** | none derived. (D1) is native on R-lin; (D3) holds in stated cases; (D4) is impossible on affine rules with coset-uniform priors (Theorem L) and unexamined on R-round; (D5) has no candidate |
| **Confrontation** | disfavoured by the recalled data (§5); formally undecided pending a first-hand margin table |

**Disposition.** Not adopted, and not recommended for adoption. On the exact linear rule it is closed by Theorem
L (unreviewed). On the non-linear branch it is an open computational question whose positive answer would still
face §5. It is recorded as candidate P-f of Bell-scope §6, now with its hypotheses and its miss conditions stated.
Identifying `c` with the wave speed remains an owner question (decision sheet, O2-C); this unit does not choose.

**Gem-finding record (§A.31).** Productivity test fixed before the derivations: a gem is a fact strictly stronger
than "the window is `Δt/√3 < d ≤ Δt/‖n̂‖₁`" that constrains the route or exposes a hidden assumption.

| # | Finding | Class |
|---|---|---|
| G1 | Lemma P: two decoupled space-time parity classes; the cone lemma is not sharp, and the 4D checkerboard hides a sector that never interacts with the visible one | NEW (assumption-watch: any argument that the checkerboard trace-out "couples" visible to hidden on the centre-free rule must say which of Π_cb3, Π_cb4 it means) |
| G2 | Lemma S: the law-level cone lags the pointwise cone by two ticks for current-slice settings | NEW |
| G3 | Theorem L: on an affine rule with a coset-uniform prior, masked ⇒ Bell-local | NEW (constrains the route; favours the obstruction, so pressure-tested: X1 shows the coset hypothesis is needed, and R-round is outside it) |
| G4 | Under the uniform prior PAD is necessary as well as sufficient for no-signalling | ELABORATING (SUBSTATE-BRIDGE-1 §3.4) |
| G5 | `1/cos θ` form; scale-free margin cut-off `√3`; duty cycle `4(1 − 1/m)` | NEW (a confrontation the route cannot avoid) |
| G6 | Partition ambiguity C-1 | NEW for Bell scope; assumption-watch for every "hidden prior" argument |

***

## 7. References to content not on `main` (§A.42 item 8)

Nothing in this file lands. Each reference is classified by what the claim attached to it uses.

| Reference | Attached to | Classification |
|---|---|---|
| `papers/Main.md` @ cac5d264 (blob `5b73da57…`): 28, 56–62, 72, 115, 131, 137, 143, 362–416, 726 | §1, §2.1, §3, §4 | support on `main` |
| `papers/SM.md` @ cac5d264 (`7d805ac8…`): 14, 66, 104–112, 126, 136, 150, 222–298, 535–557 | §1, §2, §4.3 | support on `main` |
| `papers/Substratum.md` (`e5c6f217…`) :131–133; `papers/GR.md` (`cd8d16a7…`) :166 | §1.4 | support on `main` |
| `papers/oi_lattice_code/trace_out_fractional/wave_eqn.c` (`c56e64ce…`); `papers/main_repro/lyapunov_v3.py` (`a25372b2…`) | rule definitions R-lin, R-round | support on `main` (read, not executed) |
| `…/correlation-recombination-20261107/NO-SIGNALLING.md` (`25294da4…`), `DESIGN.md` (`b3907140…`) | §1.1, §4.1 | support on `main` [W] |
| `…/oi-qm-ext-1/prepared-pair-source.md` (`9123157c…`) §§4–5; `composition-source-map.md` (`c4eeb467…`) §5.2 | (M1), (M3), (D5) | support on `main` [W]; §5.2 cited as in Bell-scope, heading read, body not re-read |
| `book/ch04-methodology.md` (`9c3888f5…`) :128 | §5 consistency note | support on `main` |
| `…/h-bell/round-hb-1-obligation-shape/preregistration.md` (`b27851ea…`) | searched for `light cone`, `wave speed`, `window`: no statement on the O2 window | provenance (negative search, this file only) |
| Bell-scope unit 1 r2, `BELL-SCOPE-UNIT1.md` (blob `5814e479…`) at `e1534b08…` on `research/bell-scope-868-20261111`, PR #1231, unreviewed at r2 | Theorem N, 𝒞_sep, (Sep), O2, P-f | **support off `main`: gap.** §3 uses Theorem N's statement to say what fails. Lemma S and Theorem L are proved here from Main:364 and Main:726 and do not use it |
| SUBSTATE-BRIDGE-1 r1, `SUBSTATE-BRIDGE-UNIT1.md` (blob `fc8ca6fb…`) at `b94b283a…` on `research/substate-bridge-1-20261111` | N1–N4, L3, (PAD) | **support off `main`: gap** for the labels; (M2) and (D1) are re-derived here |
| session file `DECISION-SHEET-MAIN-OPEN-POINTS.md` (sha256 `74f9077f…ce16`) | O2 options | off `main`; provenance |
| `probes/generic_mixedpath_checks.py` (sha256 `3bb689f6…2fd4`), output (`aa9dc84c…0f6d`), `python3 -I -B`, exit 0, 13 checks PASS | X tags | off `main`: **gap** if this record lands; the probe must land with it |
| #868 c.6794392080, c.6791565399 | authority, contract | planning records; provenance |
| Bell-test literature (§5) | raw-direct facts | **not read first-hand**; recalled. No claim of this file rests on a specific number from it |

***

## 8. Not done

- **No computation on any OI rule.** In particular: whether R-round has law-level dependence, masking or a Bell
  violation in the window; the rank condition of Theorem L(1) on any actual lattice; coefficients modulo `q` off
  the axes. These are Stage 2 (`STAGE2-PREREG.md`), not run.
- **No first-hand literature.** The margin table of loophole-free Bell tests and any sidereal analysis were not
  looked up; §5's facts are recalled.
- **Lemma P, Lemma S and Theorem L are unreviewed paper arguments.** The probe checks Theorem L on abstract linear
  models only; Lemma P and Lemma S have no computational check in this unit (they are Stage 2 controls).
- **No emergent speed for R-round.** The window uses `c_w` of the observer-level lift, whose relation to any finite
  rule is unproved (SM:232).
- **No treatment of state-dependent graphs** (O1), of R-ring, of multi-site record regions beyond what Theorem L
  covers in general, or of priors correlating generators with `Ω` (O3).
- **No choice among the partitions** (finding C-1) and no identification of `c`: both are owner questions.
- **No kernel formalization.** Lemma P and Theorem L are natural kernel targets.
- Nothing here is adopted, promoted, or proposed for the manuscripts. Finding C-1 is reported, not corrected.
