# QOPS-P2 preregistrations: P-A (T1, orbit structure) and P-C (composition across a cut)

**Standing. Plan only. Nothing here has been run, and no script exists.** This file fixes
decision rules before any outcome exists. The owner's decision approves this preregistration (U4)
and does not authorize its computation
([#1169 c.7064859041](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064859041)).
Running either plan needs separate owner authorization and an independent review of this file
first. Any change before a run is an append-only amendment under `amendments/`.

- **Goal link (§A.47).** Serves #1169 (O1, with O3 through Proposition J1 of `NOTE.md` §4). It
  decides, for stated comparison members and regions, two things:
  - whether the native gate group's orbits scale with the region and carry any invariant beyond
    the orbit indicators (P-A);
  - whether a coupling gate keeps a product of encoded constituents invariant (P-C).

  It does not decide whether layer flows are executable (FLOW), which no outcome here bears on.
- **Source definitions.**
  - The native gates are `shear_i` and `swap_i` of `SecondOrderCircuit.lean:313`, with `F` the
    member's update function.
  - The flow generators are `i(1 − P_g)/2` (`NOTE.md` §1.1).
  - Orbits, indicators, `W_O`, constituents and linking are as in `NOTE.md` §1 and QS §3.1 (the
    redesign at `f84bd746`).
- **Inputs fixed here.** The boundary is a frozen uniform `c ∈ {0, 1}` (FB). The members are:
  - U₂, the rounded rule at `q = 2` (`SM:294`);
  - L₂, the linear rule at `q = 2` (`Main:296`);
  - `R_4`, the rounded rule at `q = 4`, with `c ∈ {1, 2}` so that the ternary sector is confined
    (MEAS-Q AW-MQ-3).

  `q = 2^16` is the reference implementation (#1169 c.7064226074). It is out of reach of these
  plans, and no outcome is read as being about it.
- **Regions.** By Lemma P4, U₂ regions with fewer than three sites have only trivial shear gates.
  The regions are therefore:
  - `Λ₃`, the line of 3 sites;
  - `Λ₄`, the 2 × 2 plaquette;
  - `Λ₈`, the 2 × 2 × 2 cube (T1a only);
  - the lines of `k = 3, …, 8` sites (T1a only). For `R_4`, the lines stop at `k ≤ 4`, so that
    `q^{2k} ≤ 65 536`.

## P-A: orbit census and constituent structure (T1a, T1b)

**T1a (combinatorial; exact).** For each member, `c` and region, list the orbits of
`G = ⟨P_g⟩` on all `q^{2k}` configurations, by union-find over the gate permutations. For each
orbit, record its size and the rank of `G` on it, which is the number of `G`-orbits on ordered
pairs.

**T1b (exact linear algebra; regions with `q^{2k} ≤ 64`).** Over `ℚ(i)`, compute:
- the commutant of `{P_g}`;
- the isotypic decomposition `⊕_j V_j ⊗ ℂ^{m_j}`;
- `𝔏 = Lie_ℝ⟨i(1 − P_g)/2⟩`, by closure under brackets with an exact rank test;
- each projection `𝔨_j` on `V_j`, classified as containing `su(V_j)`, equal to `so(V_j)`, equal to
  `sp(V_j)`, or other;
- the linking relation between constituents.

**Decision rule.** The verdict text is generated from the tables.
- **T1a-exp** if, at every computed size along the line family, some orbit contains at least half
  of the configurations. **T1a-sub** otherwise. Each member and `c` is reported separately.
- **T1b-S** if some unlinked constituent with `dim V_j ≥ 4` has `𝔨_j ⊇ su(V_j)`. **T1b-R** if
  T1b-S fails and some unlinked constituent with `dim V_j ≥ 4` has `𝔨_j = so(V_j)`. **T1b-L**
  otherwise.
- **T1b-X** is recorded alongside any of these if either:
  - some orbit with `|O| ≥ 5` has rank greater than 2, so that `W_O` is reducible;
  - for two distinct orbits, `G` has more than one orbit on `O × O'`. There is then a nonzero
    intertwiner between `W_O` and `W_O'`: the two carry equivalent constituents, which may be
    linked.

  The commutant is spanned by the indicators of the orbits of `G` on `Ω × Ω`, so these are
  combinatorial invariants of the native rule. They are computed in T1a, and T1b confirms them
  (K9).

**What is pre-declared.**
- T1b-S at these sizes is expected (QS §3.1, from BQ's sensitivity run), and it is weak evidence.
- The outcomes that count against the phase-free route are T1a-sub, T1b-X and T1b-L, for the
  members and regions computed.
- Through J1, T1a bounds O3's preparation fidelity from configurations as `1 − 1/|O|`. A T1a-sub
  outcome keeps that bound away from 1 for the computed regions.

**Controls.** No verdict prints unless every control is green.
- K1, BQ's reviewed values: 2, 9, 49, and 49 without Toffoli (`AUDIT.md:117–133` at `c8d87ff4`).
- K2: for {CNOT₀₁, CNOT₁₀} at `N = 4`, the orbit `{00}` of size 1 is found, its indicator is in
  the commutant, and `dim 𝔏 = 4`, not 9.
- K3: for K1's {NOT, CNOT, SWAP} acting as `P ⊗ 1₂`, the constituent of dimension 3 has
  multiplicity 2 and `dim 𝔏 = 9`.
- K4: every `P_g` is checked exactly to be an involution and a permutation.
- K5: a commuting-only set gives an abelian `𝔏`.
- K6: gates on one fixed site only give maximal orbit size at most `q²` at every `k`, so T1a-sub.
  NOT on every bit with a CNOT chain is transitive, so T1a-exp.
- K7 (Lemma P4 as a control): on U₂, the shear gate at every end site of a line is the identity,
  and on `Λ₃` the gate list is exactly `SWAP_l, SWAP_m, SWAP_r` and the Toffoli gate of P4(4).
- K8 (Lemma P2 as a control): a gate set of single transpositions on a connected graph of 5
  points gives `dim 𝔏 = 16`.
- K9: the commutant's dimension from exact linear algebra equals the number of orbits of `G` on
  `Ω × Ω` from T1a, for every region where both are computed.

**Invariant → checkpoint (§A.41).**

| Invariant | Checkpoint |
|---|---|
| gates are permutation involutions | K4 |
| the decomposition handles multiplicities | K3 |
| a second invariant is detected | K2 |
| the native gate lists are correct | K7 |
| the closure reaches a known full algebra | K8, K1 |
| linear algebra agrees with the combinatorics | K9 |
| exact arithmetic | every rank over `ℚ(i)` uses integer elimination; no floating point |

**Outputs.** Structured JSON, per member, `c` and region: orbit sizes and ranks, the constituent
table and the verdict. Interpretation belongs to a result note (§A.44).

## P-C: encoded composition across a coupling gate

**Object.** Two copies of `Λ₃` in U₂, placed so that exactly one site of each has a neighbour in
the other. Call them `R₁` and `R₂`, with `R = R₁ ∪ R₂` (positions fixed at the preregistration
amendment that precedes any run). Two configurations are compared:
- **uncoupled**: the gates of `R₁` and `R₂`, with each region's boundary frozen;
- **coupled**: the gates of `R`, which add the cross-reading shear gates.

**Computation.** Exact, as in T1b where `q^{2|R|}` allows it; otherwise only T1a's orbit census
on `R`. Compute:
- the uncoupled orbits, which should be products, as a control;
- the coupled orbits;
- for the largest constituents `V₁` and `V₂` of the two regions, whether `V₁ ⊗ V₂` is invariant
  under the coupled `G`, and if it is not, onto which constituents the coupling gate moves it.

**Decision rule.**
- **PC-P** (product preserved) if `V₁ ⊗ V₂` is `G`-invariant in the coupled configuration.
- **PC-M** (mixed) if it is not, and the coupled constituent containing `V₁ ⊗ V₂` has dimension at
  least `dim V₁ · dim V₂`.
- **PC-L** (leaking) if it is not, and the leakage meets an orbit-indicator direction.

**Controls.**
- The uncoupled orbits must be products `O₁ × O₂` (CP11).
- A coupling by a CNOT across the cut on K1-type registers must give PC-M.
- K2–K4 of P-A.

**What it would and would not discriminate.** PC-P or PC-M is necessary for entangling encoded
registers under FLOW in the computed geometry. It is not sufficient, since the linking question
remains. No outcome bears on LT for visible composites.

## Not preregistered here

- The T3 and T7 readings are paper readings and are done in `NOTE.md` §2.
- Composition beyond P-C needs no computation at this stage.
