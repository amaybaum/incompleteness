# P0 locality sources — which locality properties follow from OI's adopted premises: rules

Research rules on a local branch cut from #834's head `55450d57`. This is not a native round, and nothing in it is
adopted. It is written and committed before the script exists. The decision rules below fix what each measurement
decides; they do not fix expected numbers.

## 1. The question

P0 (`../p0-subsystem-locality/RESULT.md`, F4–F5) found that subsystem locality (`SL-U`) coincides with operational
no-signalling at `|A| = 1` and is strictly stronger at `|A| ≥ 2`. The surplus is the absence of correlation between the
parts' hidden sectors. P0 left four sourcing obligations open (RESULT §5): the decomposition, the hidden sector's
product form, the uncoupled premise and the carriers' presuppositions.

This study asks which of the following hold on OI's own objects, a finite reversible substratum together with an
observation map and a hidden prior, and from which adopted premise each one follows:

- **(TC) tick cone.** A region's configuration after `k` ticks depends only on the initial configuration in its
  `k`-ball.
- **(FAC) factorization.** Across a cut that no rule edge crosses, `φ = φ₁ × φ₂`.
- **(INS) intervention no-signalling.**
  - Across such a cut, a permutation of region 2's configuration applied at tick 0 leaves region 1's visible law
    unchanged at every tick, for every hidden prior.
  - Across a coupled cut, the same holds at ticks below the graph distance.
- **(HI) hidden-sector independence.** Across an uncoupled cut, the joint visible law and the one-step visible kernel
  are products. This is the `𝒪₀`-level content of P0's F5 surplus.
- **(SEL) selection independence.** Conditioning on region 2's visible value leaves region 1's visible law unchanged.
  This is correlation, not signalling, and is recorded separately from INS.

## 2. The adopted premises the study may use

Each item is cited at `D₀ = 3519213a` (main) and used only as stated:

| premise | where | status in the corpus |
| --- | --- | --- |
| second-order leap `(p, c) ↦ (c, F c − p)` on `ι → V × V` | SubstratumInterfaceAudit.lean:79 | definition of the substratum |
| finite-range rule: `F c i` depends only on `c` on `N i` | SecondOrderLayer.lean:198–203 (`Rule.dep`) | part of the structure |
| bounded coupling degree | (A3) Substratum.md:96; SubstratumInterfaceAudit.lean:91 | structural assumption |
| nearest-neighbour range | SM.md:226 | adopted, "an assumption beyond A3" |
| linearity (A5) | SubstratumInterfaceAudit.lean:102; Main.md:708 (vii) | posit |
| the causal cone | RegionTower.lean:283, :304 (`iterate_dependsOnlyOn_ball`, `readout_unaffected_outside_ball`) | kernel theorem |
| the measure: uniform on the actual orbit; the counting measure selected as maximal entropy compatible with the records | Main.md:56, :62; Main.md:708 (iv); CanonicalMeasure.lean | Lemma 3 and posit (iv) |
| structured hidden priors as realization data | Main.md:60 | admitted by the text |
| the registered component is the current one; the previous one is hidden | F2 thread H, E1(a), on the research branch; the phase-space pair `(x(t−1), x(t))` is SM.md:106 | a reading used by E1, not adopted |
| the observer theory consumes nothing of A3–A6 | SubstratumInterfaceAudit.lean:779 (`obsTheory_rule_independent`) | kernel theorem |

Not adopted, and used only as candidate additions or as P0's notions: `SL-U`, product hidden anchors, and E1-L.

## 3. Objects

- **Sites and rules.** Linear, link-coupled second-order rules over `V = ℤ/q`, `F c i = Σ_{j ∈ N i} M_ij c_j`.
- **Regions.** A region is a set of sites. A cut is uncoupled when no `j ∈ N i` lies across it.
- **Visible and hidden.** In each region the visible datum is the tuple of current components `c` of the region's sites;
  the hidden datum is the tuple of previous components `p`.
- **Hidden priors (ensembles).** A law on `Conf` at tick 0:
  - **E-cnt**: the counting measure on `Conf`;
  - **E-reg**: the uniform law on `O₁ × O₂`, with `Oₖ` an orbit of `φₖ`. This is the maximal-entropy invariant law whose
    regional records are the regional orbits;
  - **E-orb**: the uniform law on one orbit of `φ`, Lemma 3's law on the orbit of the actual microstate. Every orbit of
    every frozen configuration is used;
  - **E-pri**: a structured prior, uniform on `{p₁ = p₂}` across the cut, with `c` free (Main.md:60);
  - **E-pt**: point masses, for the cone and INS checks.
- **Interventions.** On region 2 at tick 0:
  - translations `(p, c) ↦ (p + a, c + b)` at one site;
  - the exchange `(p, c) ↦ (c, p)` at one site;
  - one transposition of two configurations of one site, which is non-affine.
- **Visible laws.**
  - The joint visible law at tick `t`.
  - The one-step kernel `Γ_t(v' | v)`, defined where `v` has positive weight.
  - The two-time law of `(v_t, v_{t+1})`.

## 4. Frozen configurations

| id | sites, rule | cut | use |
| --- | --- | --- | --- |
| `U-free(q)` | two isolated sites (`N = ∅`), `q ∈ {3, 5}` | between the sites, uncoupled | FAC, INS, HI, SEL; the free layer of F2 |
| `U-edge(q, α, β)` | two disjoint 2-site edges with couplings `α`, `β`; `q = 3`, `α, β ∈ {1, 2}` | between the edges, uncoupled | FAC, INS, HI, SEL |
| `FAM(q)` | every ordered pair from {isolated site, 2-site edge `α ∈ 1..q−1`}; `q ∈ {3, 5}` | uncoupled | W4's criterion, exhaustively |
| `C-chain` | open chain of 6 sites, nearest-neighbour, `α = 1`, `q = 3` | regions `{0}` and `{5}`, distance 5 | TC, coupled INS |
| `C-cut` | open chain of 4 sites, nearest-neighbour, `α = 1`, `q = 3` | `{0,1} | {2,3}`, one crossing edge | FAC and INS countercontrols |

## 5. Written statements to be checked [W]

- **W1 (FAC).** If no edge crosses the cut, `φ = φ₁ × φ₂`, because the leap acts sitewise in `(p, c)` with `F c i`
  read on `N i`.
- **W2 (INS, every prior).** Under `φ = φ₁ × φ₂`, region 1's marginal at tick `t` is the push-forward of `μ`'s region-1
  marginal by `φ₁ᵗ`. A region-2 intervention does not change that marginal. This holds for every `μ`, correlated or
  not.
- **W3 (HI under E-cnt and E-reg).** The uniform law on a product of invariant sets is a product of invariant laws. So
  every visible law it induces under `φ₁ × φ₂` is a product.
- **W4 (orbit criterion).** The joint orbit of `(x₁, x₂)` has size `lcm(|O₁|, |O₂|)` and projects onto `O₁` and `O₂`.
  Its uniform law is a product iff the orbit is `O₁ × O₂`, that is, iff `gcd(|O₁|, |O₂|) = 1`.
- **W5 (maximal entropy with regional records).** Among invariant laws supported on `O₁ × O₂`, the uniform law on
  `O₁ × O₂` has the largest support and so the largest entropy. Maximal entropy compatible with regional records
  therefore selects the product.
- **W6 (identical copies).** For identical uncoupled regions and `x₂ = x₁` with `|O(x₁)| > 1`, the gcd is `|O(x₁)|`, so
  the orbit law is correlated.

## 6. Checks and decision rules

All arithmetic is exact (integers and `Fraction`). Each token prints from the measurements.

| cell | positive token | rule |
| --- | --- | --- |
| TC | `LS-TC` | On `C-chain`, from every point mass, each tested intervention at site 5 leaves site 0's configuration unchanged for `t < 5`, and some intervention changes site 0's visible value at `t = 5`. K-cone-neg passes |
| FAC | `LS-FAC` | `φ = φ₁ × φ₂` exhaustively on `U-free`, `U-edge` and `FAM`, and fails on `C-cut` |
| INS | `LS-INS-ALL-PRIORS` | On `U-free` and `U-edge`, every tested intervention leaves region 1's joint visible law at `t = 0..8` and its two-time law unchanged. This holds under E-cnt, every E-reg, every E-orb, E-pri and every point mass. On `C-cut`, some point mass shows a change at `t = 1` (non-vacuity) |
| HI-default | `LS-HI-DEFAULT` | Under E-cnt and every E-reg on `U-free` and `U-edge`, the joint visible law at `t = 0..8` and each one-step kernel are products |
| HI-orbit | `LS-HI-ORBIT-FAILS` | (a) On `FAM(3)` and `FAM(5)` every joint orbit's uniform law is a product iff the gcd of the regional orbit lengths is 1, with no exception. (b) Some E-orb law on `U-free` or `U-edge` has a non-product joint visible law or one-step kernel, while INS holds for it |
| HI-prior | `LS-HI-PRIOR-FAILS` | E-pri on `U-free(3)` gives a non-product one-step kernel while INS holds |
| SEL | `LS-SEL-SPLIT` | Under E-cnt and E-reg, conditioning on region 2's visible value never changes region 1's visible law. Under some E-orb or E-pri law, it does |

**Reading.** When `LS-INS-ALL-PRIORS`, `LS-HI-DEFAULT`, `LS-HI-ORBIT-FAILS` and `LS-HI-PRIOR-FAILS` all print, the study
prints `LS-SPLIT`:

> Across an uncoupled cut of a finite-range substratum, intervention no-signalling follows from the rule's dependency
> structure for every hidden prior. Hidden-sector independence follows from the counting measure, or from maximal
> entropy with regional records. It does not follow from Lemma 3's law on the actual orbit when the regional periods
> share a factor, nor from structured realization priors.

Any other combination prints the tokens that hold and `LS-NOT-SPLIT`.

## 7. Controls

| id | content |
| --- | --- |
| K0 | standard library only; `Fraction` arithmetic; two runs byte-identical |
| K-leap | the implemented step equals `(p, c) ↦ (c, F c − p)` on hand-computed instances, and is a bijection on every frozen `Conf` |
| K-cone-neg | a mutated rule whose `F` at site 0 reads site 3, outside the declared `N 0`, makes the TC check fail on `C-chain` |
| K-INS-neg | INS fails on `C-cut` (also a cell condition) |
| K-prod | the product test accepts a constructed product law and rejects a constructed correlated law. Two independent tests, all 2×2 minors and entrywise comparison with the product of marginals, agree on every law tested |
| K-orbit | orbits computed by iteration and by union-find over `x ↦ φ x` agree on every configuration of `FAM` |
| K-free | the isolated-site step has order 4 on `V × V \ {0}` at `q = 3, 5` (the coupling-free leap) |

A token printed over a failed control is void, and the study then prints `VOID`.

## 8. Invariants and checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| the rules precede the script | this file's commit precedes the script's first commit; its blob is quoted in the result |
| the dynamics is the kernel's leap | K-leap |
| the checks are not vacuous | K-cone-neg, K-INS-neg, K-prod |
| the orbit structure is computed, not assumed | K-orbit; W4 is checked against the computed orbits, not used to compute them |
| replayable | K0 |

## 9. Non-claims fixed in advance

- No locality principle is adopted, and none is proposed for adoption.
- Nothing here concerns Track B's dilation carriers `𝒪₁`–`𝒪₃`. The laws are visible laws of the deterministic
  substratum under a prior. The relation to P0's pure-anchor dilations is stated, not tested.
- Coupled cuts are tested only for the cone (TC, coupled INS). HI across coupled cuts is out of scope.
- Bell-type preparations, which Main.md:392 and SM.md:110 allow to carry preparation-indexed non-local edges, are out
  of scope. So is H-Bell.
- Sub-tick locality is out of scope. The corpus already records its independence from tick-level data:
  - F2-1 RESULT.md:304–315, two uncoupled sites interacting at sub-period times under the composite logarithm [X];
  - ROADMAP.md:1522, "Executable intermediate layer flow" **INDEPENDENT**.
