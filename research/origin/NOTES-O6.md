# NOTES-O6 — the stage-crossing generator against O3-T5's three requirements

Thread `research/origin`, round 2, node O6. Base L = `9f9f8257`; kernel paths under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels as in NOTES-O1. Script: `experiments/o6_tower.py`
(decision rule fixed in the header before run 1; one pre-run edit before any run: K9's nonnegativity check changed
from a sampled comparison to the exact identity (9/16) cos t + (3/16) cos 3t = (3/4) cos³ t, header line updated
with it; run 1 green, `VERDICT EXCLUSIVE-ON-PASSIVE-JOINT-ON-INVASIVE`; replay byte-identical). Design module:
`OriginPassive.lean` Sections C and D (RESULTS, LOG). Received and checked against: HO-2 v1 item HO-2c (one-token
clause, CONDITIONAL on [L]); HO-8 v1 (targets at their labels).

**Productivity test, fixed before starting (§A.31).** A finding counts only if it is strictly stronger than
"F-D3: the generator must cross stages" and either decides whether O3-T5's three requirements are compatible
(on passive towers, and in general) or constrains the observation law a field-neutral drive needs.

## 0. Verdict

1. **On passive towers the three requirements are mutually exclusive.** With finite rank, passive and repeatable
   native observation and reversible data, every extreme point of the completed chart body is outcome-deterministic
   for every protocol effect, so there are at most 2^d of them and every reversible datum — stage-crossing or not —
   has finite order (T1). Crossing stages, which the kernel already requires of an infinite-order datum
   (`not_stagePreserving_of_infiniteOrderOn` [K CompositionOrder.lean:378]), does not help on a passive tower.
2. **What the generator must do to the frame readout (T2).** An infinite-order datum on a finite-rank body forces
   all but at most 2^d pure states to be outcome-random for some protocol effect; its orbits carry pure states into
   such outcome-random pure states (in the instance: pure frame states into pure states with frame probability
   strictly between 0 and 1); with a repeatable readout, observation is invasive at all of them (Lemma P).
3. **With invasive repeatable observation the requirements hold together (exact instance, I).** On the circle
   substratum, a readout that records the half-circle outcome and re-prepares the hidden angle with the cosine
   density gives a tower of rank 3 at every stage (the disk), the rotation by a (cos a = 3/5) is an infinite-order
   stage-crossing datum, the readout is repeatable and invasive, and the owner's witness is exact for the closure
   member R(π/2) — never for a stage datum. On the sphere the same law gives rank 4 (the ball) and OFF.
4. **What finite rank asks of the invasive law (L).** The rank is the number of Fourier modes of the readout's
   response: conditioning and the uniform re-preparation law give ranks 2^m + 1 on the dyadic grids (growing);
   the cosine law gives 3; at minimal rank, repeatability forces the response (1 + cos β)/2.
5. **O5 and O6 meet at one premise.** The observation law that makes O6-I work is a measure-and-re-prepare law —
   KB-D in continuous form — and its exclusivity is what the stated access excludes (O5-T1a): adding the passive
   conditioning back restores the growing rank (P1). The field-neutral Continuous Origin and the source of KB-D are
   one open question.

## 1. T1 — passive towers: finite rank and infinite order exclude each other

**Setting.** A protocol tower D (OI-STAGE's PT or CT form [A oistage §1]) with FiniteRank and a completion chart
C; K = `chartBody C`, compact and convex (`chartBody_isCompact`, `chartBody_convex` [K TransitiveBody.lean:109,
:80]). The native observation is (P) passive — observe-and-forget equals the idle step, Σ_v τ_v = W (exact A5 for
every tower built by conditioning a classical substratum [A oistage §7]) — and (R) repeatable — the pre-step
conditioned state reads its outcome surely; the time step and the actions have inverse data, so they act as body
automorphisms (`preservesBody_inducedEquiv` [K CompletionAction.lean:352]). Both (P) and (R) pass to the
completed body by continuity (both sides affine and continuous in the chart, equal on preparations) [W].

**T1.** (i) Every extreme point of K is outcome-deterministic for every protocol effect. (ii) K has at most 2^d
extreme points (d the chart dimension); it is a polytope. (iii) Every reversible datum respecting affine relations,
whether or not it preserves stages, induces an automorphism of finite order on K. (iv) Hence no OPS-Γ datum, no
circle in the closure of any datum, no `ElementaryDrivability` on K.

*Proof.* (i) [W] At an extreme point ω, the observe-and-forget decomposition W⁻¹(Σ_v τ_v ω) = ω writes ω as a
mixture of the conditioned states with the outcome probabilities as weights (NG2's step 2: every extreme ray is an
eigenvector of each M_v = W⁻¹τ_v); by (R) the conditioned state of outcome v reads v surely, so a mixture with two
positive weights would be a proper convex combination of distinct body states, and ω is deterministic — Lemma P,
the abstract step being `lemmaP_extreme` [D]. The post-observation state is then Wω, extreme again; actions are
automorphisms, so by induction along the protocol every outcome is deterministic. (ii) Finitely many protocol
labels a₁ … a_d coordinatize the chart injectively (DRIVE §2.2 step 2 [A]); on deterministic points these
coordinates are 0 or 1, so the extreme points inject into {0, 1}^d: `extremePoints_finite_of_binary` [D]. (iii)
`finiteOrderOn_chartBody_of_binary` [D]: on the chart body, binary injective coordinates on the extreme points give
`FiniteOrderOn (chartBody C) (inducedEquiv C …)` for every reversible datum — a composition of
`finiteOrderOn_of_finite_extremePoints` [D] (a common period of the extreme points, `exists_return`,
`exists_common_period` [K CompositionOrder.lean:149, :171], and Krein–Milman) with the landed chart lemmas.
(iv) `not_infiniteOrderOn_chartBody_of_binary` [D]; a circle in the closure of ⟨g⟩ would give g infinite order
(DRIVE Γ2 [A]). ∎

**Relation to the corpus.** NG2 excluded strictly convex bodies on passive towers with a reversible time step;
T1 excludes every infinite-order datum on every finite-rank passive tower. F-D3, kernelized as
`finiteOrderOn_of_stagePreserving` / `not_stagePreserving_of_infiniteOrderOn` [K CompositionOrder.lean:348, :378],
says an infinite-order datum crosses stages; T1 says that on passive towers no datum has infinite order at all.
HO-2c (received, CONDITIONAL on [L]) says directed unions of finite stage-preserving groups do not give an off-axis
drive; T1 is consistent with it and does not use it. Cross-propagation to HO-8: the K∞-Trans target
(boundary-transitive or dense-orbit family) is impossible on a passive finite-rank body of dimension ≥ 2, since a
polytope has non-extreme boundary points (`not_boundaryTransitive_of_nonextreme_boundary` [K
TransitiveBody.lean:301], applied [W]).

## 2. T2 — what an infinite-order generator must do to the frame readout

Let D have FiniteRank, a repeatable native readout and reversible data, and let g be a reversible datum respecting
affine relations with infinite order on K — equivalently (DRIVE Γ2 [A]; Cartan's closed-subgroup theorem [L]) the
closure of ⟨g⟩ contains a nontrivial one-parameter subgroup. Then [W + D]:
(a) K has infinitely many extreme points (by [D] `finiteOrderOn_of_finite_extremePoints`), and at most 2^d of them
    are outcome-deterministic for every protocol effect (binary injective coordinates); so all but finitely many
    pure states are outcome-random for some protocol effect;
(b) every infinite g-orbit of a pure state contains infinitely many outcome-random pure states;
(c) at every outcome-random pure state the native observation is invasive (Lemma P, given repeatability).
In words: the generator must carry pure states into pure states on which the frame readout (or a protocol built on
it) is outcome-random, infinitely often, and the readout must disturb them. The converse fails: invasive
observation does not give an infinite-order datum — the KB-D octahedron is invasive and its reversible group has
order 24 (O3-T3 [X C4]).

## 3. I — the smallest exact tower meeting all three requirements

Chart dimension 2 is the smallest in which a compact convex body has an automorphism of infinite order (in
dimension 1 a segment has the identity and the flip) [W]; the disk is the instance.

- **Substratum and law.** The circle S¹ (infinite), its rotation-invariant measure; readout along u: outcome + iff
  cos(λ − u) > 0. Re-preparing law: after outcome ±u, λ is re-sampled from ρ_{±u}(λ) = cos(λ ∓ u)/2 on the
  outcome's half-circle (the Kochen–Specker density on the circle [L, Kochen–Specker 1967]). Rotations of λ are
  bijections of the substratum (stated access); the re-preparing readout is not (A5 makes conditioning the native
  readout).
- **Response.** P(+u | ρ_ψ) = (1 + cos(u − ψ))/2 exactly, on both halves of [0, 2π]; the density is normalized and
  nonnegative [X K1].
- **Finite rank.** Every protocol probability is affine in the barycenter of the preparation's ψ-distribution,
  because each readout re-prepares; the table of single and two-step readouts has rank 3 at every stage
  n = 1 … 10 [X K2]. Chart body: the unit disk.
- **Datum.** g = rotation by a, cos a = 3/5: e^{ia} = (3 + 4i)/5 has minimal polynomial 5x² − 6x + 5, not monic
  over Z, so it is not a root of unity; R(a)^k ≠ 1 for k ≤ 200 [X K3]. It crosses stages: stage n = directions
  {ka : |k| ≤ n}, g(stage n) ⊆ stage n + 1, (n + 1)a ∉ stage n [X K4] — as `not_stagePreserving_of_infiniteOrderOn`
  [K CompositionOrder.lean:378] requires.
- **Readout.** Repeatable (P(+u | ρ_u) = 1) and invasive (observe-and-forget along u = 0 sends the Bloch vector
  (3/5, 4/5) of ρ_a to (3/5, 0)); the pure states ρ_{ka}, k = 1 … 200, are outcome-random for the frame readout
  [X K5] — T2's requirement, met.
- **Witness.** With the closure member R(π/2): (P_coh, P_deph) = (1, 1/2) exactly. With the stage data g^k:
  P_deph = (1 + cos² ka)/2 > 1/2, V_k = sin²(ka)/2 < 1/2, k = 1 … 200 [X K6]: the exact balanced mixer is
  completion-valued, never a stage operation (consistent with DRIVE §3.3).
- **OFF and the ball.** On the disk every J ∈ O(2) normalizes SO(2) (DRIVE X-OFF [A]). On the sphere the same law,
  ρ_ψ(λ) = (ψ·λ)⁺/π, gives P(+u | ρ_ψ) = (1 + ψ·u)/2 (projection to the equatorial disk: area π/2 + (π/2) cos β,
  symbolic), rank 4 on 18 rational unit vectors, and OFF-Γ′ for g = R_z(a), J = R_x(π/2), m = 1 … 60 [X K7].
**Status.** The three requirements of O3-T5 (finite rank of an infinite-substratum completion, an infinite-order
stage-crossing datum with OFF, invasive repeatable observation) are jointly satisfiable — CONDITIONAL on the
re-preparing law, which is outside the stated access.

## 4. L — what finite rank asks of the invasive law

On the circle with a rotation-covariant law the table is circulant in u − ψ, so on a uniform grid its rank is the
number of nonzero discrete Fourier coefficients of the response f [W].
- Passive conditioning: every elementary arc of the dyadic grid {jπ/2^m} is a reachable preparation (the
  intersection of two grid half-circles), and the table has rank 2^m + 1 = 3, 5, 9, 17, 33, 65 for m = 1 … 6
  [X P1]. The passive tower on this substratum has no finite-rank completion, as T1 requires of a passive tower
  with an infinite-order datum.
- Uniform re-preparation (response 1 − |β|/π): the same ranks [X K8].
- Cosine re-preparation: rank 3 [X K2].
- With f(0) = 1 (repeatable) and f(β) + f(β + π) = 1 (two outcomes), a degree-1 response is forced to be
  (1 + cos β)/2 [X K9]. Finite rank alone does not force it: 1/2 + (9/16) cos β − (1/16) cos 3β is repeatable, its
  re-preparation density −f′(t + π/2) = (3/4) cos³ t is nonnegative, and its table has rank 5 [X K9].

## 5. Classification (§A.31)

- **NEW, O6-N1.** T1: on passive towers finite rank and an infinite-order datum exclude each other, stage crossing
  or not (strictly stronger than NG2 and F-D3); the finite-order step is a design-run composition with the landed
  chart lemmas.
- **NEW, O6-N2.** T2: an infinite-order generator forces all but 2^d pure states outcome-random, and observation
  invasive at them; invasive observation is necessary, not sufficient (KB-D octahedron).
- **NEW, O6-N3.** I: the three requirements of O3-T5 hold together, with a repeatable readout, in an exact
  classical-substratum tower whose readout re-prepares (the Kochen–Specker law on the circle and the sphere); the
  exact balanced mixer is completion-valued.
- **NEW, O6-N4 (assumption-watch marker).** The field-neutral Continuous Origin and the source of KB-D are one
  premise: an exclusive measure-and-re-prepare readout. Finite rank constrains it to finitely many response
  harmonics; minimal rank selects the cosine law.
- **CONFIRMING, O6-C1.** F-D3 (`not_stagePreserving_of_infiniteOrderOn`), HO-2c's one-token clause, oistage R1
  (passive rotation tower with growing rank).

## 6. Scope (skeptical pass on the favourable branch O6-I)

The instance's substratum is a circle (a sphere for OFF) with its rotation-invariant measure, not OI's cubic lattice with
the wave equation, and its readout law is chosen. O6-I shows that O3-T5's three requirements are compatible, with a
repeatable readout, once a re-preparing law is granted; it does not show that OI's own substratum carries such a law,
which is part of the open premise (O6-V). The infinite-order datum is a rotation of the substratum, a bijection of the
stated kind; the only element outside the stated access is the readout law.
